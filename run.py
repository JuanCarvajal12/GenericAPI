"""
@carva

when deving on VSCode in my machine, change interpreter with
(Ctrl+Shift+P) | >Python:Select Interpreter | 'fastapidev' conda

run with
      uvicorn run:app --reload --port 3000
--reload enables auto-refreshing when updating code.
"""

#%---
from fastapi import FastAPI, Header, File, Body
from routes.v1 import app_v1
from routes.v2 import app_v2
from routes.old import app_old

app = FastAPI()

app.mount("/old", app_old)
app.mount("/v1", app_v1)
app.mount("/v2", app_v2)