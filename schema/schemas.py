def individual_serial(todo) -> dict:
    """returns a dict for mongodb json return. This helps us to work it within our application"""
    return {
        "_id" : str(todo["_id"]),
        "name" : todo["name"],
        "description" : todo["description"],
        "todo_number" : todo["todo_number"],
        "complete" : todo["complete"]
    }

def group_serial(todos)->list[dict]:
    """returns a list of todos converting it to a list of dicts"""
    return [individual_serial(todo) for todo in todos]