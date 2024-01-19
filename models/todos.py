from pydantic import BaseModel

class Todo(BaseModel):
    name : str
    todo_number : int
    description : str
    complete : bool
    