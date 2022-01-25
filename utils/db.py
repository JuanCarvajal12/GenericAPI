# import asyncio
from utils.db_object import db

# Tested execute function with this query
# query = "insert into products values(:ref, :name, :category, :supplier, :year)"

# values_m = [{'ref': 'ref3', "name": 'prod3', "category": 'cat3', "supplier": "supplier1", "year": 2019},
#           {'ref': 'ref2', "name": 'prod2', "category": 'cat2', "supplier": "supplier2", "year": 2019}]

# values_o = {'ref': 'ref1', "name": 'prod1', "category": 'cat1', "supplier": "supplier1", "year": 2019}

async def execute(query, is_many,values=None):
    if is_many:
        await db.execute_many(query=query, values=values)
    else:
        await db.execute(query=query, values=values)

# tested fetch function with this query

query_1 = "SELECT * FROM products WHERE ref=:ref"
query_2 = "SELECT * FROM products"
values = {"ref": "ref1"}

async def fetch(query, is_one, values=None):
    if is_one:
        result = await db.fetch_one(query=query, values=values)
        if result is None:
            out = None
        else:
            out = dict(result)
    else:
        result = await db.fetch_all(query=query, values=values)
        if result is None:
            out = None
        else:
            out = []
            for row in result:
                out.append(dict(row))
    return out

# loop = asyncio.get_event_loop()
# loop.run_until_complete(execute(query, False, values_o))
# loop.run_until_complete(execute(query, True, values_m))
# print(loop.run_until_complete(fetch(query_1, True, values)))
# print(loop.run_until_complete(fetch(query_2, False)))


