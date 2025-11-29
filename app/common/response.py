def success_response(data, message="Success"):
    # Nếu là Pydantic object → convert sang dict
    if hasattr(data, "dict"):
        data = data.dict()
    # Nếu là list Pydantic object → convert từng phần tử
    elif isinstance(data, list) and len(data) > 0 and hasattr(data[0], "dict"):
        data = [item.dict() for item in data]

    return {
        "status": "success",
        "message": message,
        "data": data
    }

def error_response(message="Error", code=400):
    return {
        "status": "error",
        "message": message,
        "code": code,
        "data": None
    }
