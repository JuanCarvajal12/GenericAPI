from utils.db import execute, fetch


async def db_check_token_user(user):
    query = """
    SELECT * FROM users WHERE
        username = :username"""
    values = {"username": user.username}

    result = await fetch(query, False, values)
    return result

async def db_check_jwt_username(username):
    query = """
    SELECT * FROM users WHERE
        username = :username"""
    values = {
        "username": username,
        }

    result = await fetch(query, True, values)
    if result is None:
        return False
    else:
        return True

async def db_insert_personel(user):
    query = """insert into personel(username, password, mail, role)
               values(:name, :password, :mail, :role)"""
    values = dict(user)

    await execute(query, False, values)

async def db_check_personel(username, password):
    query = """
    SELECT * FROM personel WHERE
        username = :username AND
        password = :password"""
    values = {"username": username, "password": password}
    result = await fetch(query, True, values)

    if result is None:
        return False
    else:
        return True

async def db_get_product_with_ref(ref):
    query = """
    SELECT * FROM products WHERE
        ref = :ref"""
    values = {"ref": ref}

    product = await fetch(query, True, values)
    return product

async def db_get_product_with_ref(ref):
    query = """
    SELECT * FROM products WHERE
        ref = :ref"""
    values = {"ref": ref}

    product = await fetch(query, True, values)
    return product

async def db_get_supplier_with_name(s_name):
    query = """
    SELECT * FROM suppliers WHERE
        name = :name"""
    values = {"name": s_name}

    supplier = await fetch(query, True, values)
    return supplier

async def db_get_supplier_with_id(s_id):
    query = """
    SELECT * FROM suppliers WHERE
        id = :id"""
    values = {"id": s_id}

    supplier = await fetch(query, True, values)
    return supplier

async def db_patch_supplier_name(id, new_name):
    query = """
    UPDATE suppliers SET
        name=:name WHERE
        id=:id"""
    values = {"name": new_name, "id": id}
    await execute(query, False, values)