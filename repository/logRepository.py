def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "data": dir
    }

def lista(entity) -> list:
    return [item for item in entity]