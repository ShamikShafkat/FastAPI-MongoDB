from pydantic import BaseModel,EmailStr,Field

class Todo(BaseModel):
    name : str = Field(...)
    todo_number : int = Field(...,ge=0)
    description : str = Field(...)
    complete : bool = Field(False)
    