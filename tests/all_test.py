from starlette.testclient import TestClient
# I have a problem with my venv or the setting in vscode that
# bugs local imports when executing from python. This is not the best way, but
# allows me to continue...
try:
    from run import app
except Exception as e:
    import sys
    from os import getcwd
    sys.path.append(getcwd())
    from run import app
from utils.db import fetch, execute
import asyncio
from utils.security import get_hashed_password
from models.user import User

client = TestClient(app)
loop = asyncio.get_event_loop()

def insert_user(username, password, mail="a@b.c", role="admin"):
    query = """
        INSERT INTO
            users(username, password, mail, role)
            values(:username, :password, :mail, :role)
        """
    hashed_password = get_hashed_password(password)
    values = {
        "username": username,
        "password": hashed_password,
        "mail": mail,
        "role": role
        }
    
    loop.run_until_complete(execute(query, False, values))

def check_personel(username, password):
    query = """
        SELECT * FROM
            personel
        WHERE
            username=:username AND
            password=:password"""
    values = {"username": username, "password": password}
    result = loop.run_until_complete(fetch(query,True,values))
    if result is not None:
        return True
    else:
        return False

def get_auth_header():
    insert_user("test_user", "test_pass")

    response = client.post("/token", 
            {
            "username": "test_user",
            "password": "test_pass"
            })
    jwt_token = response.json()['access_token'] 
    auth_header = {"Authorization": f"Bearer {jwt_token}"}

    return auth_header


def clear_db():
    querys = ["""DELETE FROM users;""", """DELETE FROM suppliers;""",
        """DELETE FROM personel;""", """DELETE FROM products;"""]
    
    for query in querys:
        loop.run_until_complete(execute(query, False))

def test_token_successful():
    insert_user("test_user", "test_pass")

    response = client.post("/token", 
            {
            "username": "test_user",
            "password": "test_pass"
            })

    assert response.status_code == 200
    assert "access_token" in response.json()

    clear_db()
    

def test_token_unauthorized():
    insert_user("test_user", "test_pass")

    response = client.post("/token", 
            {
            "username": "test_user",
            "password": "test_pass_wrong"
            })

    assert response.status_code == 401

    clear_db()

def test_post_user():
    user_dict = {
        "name": "sample_username",
        "password": "sample_password",
        "mail": "a@b.c",
        "role": "personel"
    }
    auth_header = get_auth_header()
    response = client.post("/v2/user",
        json=user_dict, headers=auth_header)

    assert response.status_code == 201
    assert check_personel("sample_username", "sample_password")

    clear_db()

def test_post_user_wrong_email():
    user_dict = {
        "name": "sample_username",
        "password": "sample_password",
        "mail": "not.valid",
        "role": "personel"
    }
    auth_header = get_auth_header()
    response = client.post("/v2/user",
        json=user_dict, headers=auth_header)

    assert response.status_code == 422
    
    clear_db()