# Importing all the neccessary packages.
from pydantic import BaseModel

# Classes used in huey tasks.
class pair(BaseModel):
    key: str
    value: str

class val(BaseModel):
    value: str