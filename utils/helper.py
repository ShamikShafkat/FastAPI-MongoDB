def response_body(success:bool,message:str,data):
    return {
        "success" : success,
        "message" : message,
        "data" : data
    }