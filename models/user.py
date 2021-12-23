from pydantic import BaseModel
import enum
from fastapi import Query

# email-regex
email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

# this enum.Enum class sets the possibilities.
class Role(str, enum.Enum):
    admin: str = 'admin'
    personel: str = 'personel'

# user class
class User(BaseModel):
    name: str
    password: str
    mail: str = Query(..., regex=email_regex) # if mail is needed
    #mail: str = Query(None, regex=email_regex) # if mail isn't needed
    role: Role # one between some possibilities defined in class Role
