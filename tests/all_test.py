from starlette.testclient import TestClient
from run import app
from utils.db import fetch, execute
import asyncio
from utils.security import get_hashed_password

client = TestClient(app)
loop = asyncio.get_event_loop()

def insert_user(username, password, mail="a@b.c", role="admin"):
    query = """
        INSERT INTO
            users(username, password, mail, role)
            values(:username, :password, :mail, :role)
        """
    password = get_hashed_password(password)
    values = {
        "username": username,
        "password": password,
        "mail": mail,
        "role": role
        }
    
    loop.run_until_complete(execute(query, False, values))

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