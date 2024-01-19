from fastapi import APIRouter,status
from models.todos import Todo
from config.database import collection_name
from schema.schemas  import individual_serial
from bson import ObjectId
from utils.helper import response_body

"""creates a router object for routes"""
router = APIRouter()

"""a get request end point for all the todos in the appication. Here @router is a decorator function."""
@router.get("/",status_code=status.HTTP_200_OK)
async def get_todos():
    try:
        cursor = collection_name.find()
        todos_list = []
        for document in await cursor.to_list(length=100):
            todos_list = todos_list + [individual_serial(document)]
        return response_body(success=True,message="Here are your all todos.",data=todos_list)
    except Exception as e:
        print(e)
        return response_body(success=False,message=str(e),data=None)
    

@router.post("/",status_code=status.HTTP_201_CREATED)
async def post_todo(todo : Todo):
    try:
        await collection_name.insert_one(dict(todo))
        return response_body(success=True,message="Your todo has been posted",data=None)
    except Exception as e:
        print(e)
        return response_body(success=False,message=str(e),data=None)
            
@router.put('/{id}',status_code=status.HTTP_200_OK)
async def update_todo(id:str,todo:Todo):
    try:
        new_todo = await collection_name.find_one_and_update({"_id":ObjectId(id)},{
            "$set" : dict(todo)
        },
        return_document = True
        )
        return response_body(success=True,message="Your todo has been updated",data=individual_serial(new_todo))
    except Exception as e:
        print(e)
        return response_body(success=False,message=str(e),data=None)

@router.delete("/{id}",status_code=status.HTTP_200_OK)
async def delete_todo(id:str):
    try:
        await collection_name.find_one_and_delete({"_id":ObjectId(id)})
        return response_body(success=True,message="Your todo deleted successfully",data=None)
    except Exception as e:
        print(e)
        return response_body(success=False,message=str(e),data=None)