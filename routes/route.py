from fastapi import APIRouter,status
from models.todos import Todo
from config.database import collection_name
from schema.schemas import group_serial
from schema.schemas  import individual_serial
from bson import ObjectId
from utils.helper import response_body

"""creates a router object for routes"""
router = APIRouter()

"""a get request end point for all the todos in the appication. Here @router is a decorator function."""
@router.get("/",status_code=status.HTTP_200_OK)
async def get_todos():
    try:
        todos = collection_name.find()
        return response_body(success=True,message="Here are your all todos.",data=group_serial(todos))
    except Exception as e:
        print(e)
        return response_body(success=False,message=str(e),data=None)
    
@router.post("/",status_code=status.HTTP_201_CREATED)
async def post_todo(todo: Todo):
    try:
        collection_name.insert_one(dict(todo))
        return response_body(success=True,message="Your todo has been posted",data=None)
    except Exception as e:
        print(e)
        return response_body(success=False,message=str(e),data=None)
        
@router.put('/{id}',status_code=status.HTTP_200_OK)
async def update_todo(id:str,todo:Todo):
    try:
        new_todo = collection_name.find_one_and_update({"_id":ObjectId(id)},{
            "$set" : dict(todo)
        },{
            "return_original" : False
        })
        return response_body(success=True,message="Your todo has been updated",data=individual_serial(new_todo))
    except Exception as e:
        print(e)
        return response_body(success=False,message=str(e),data=None)

@router.delete("/{id}",status_code=status.HTTP_200_OK)
async def delete_todo(id:str):
    try:
        collection_name.find_one_and_delete({"_id":ObjectId(id)})
        return response_body(success=True,message="Your todo deleted successfully",data=None)
    except Exception as e:
        print(e)
        return response_body(success=False,message=str(e),data=None)