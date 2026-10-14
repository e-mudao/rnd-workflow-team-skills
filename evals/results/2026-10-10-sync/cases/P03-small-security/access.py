def can_read(user, resource):
    return user["tenant"] == resource["tenant"] and (user["id"] == resource["owner"] or user["admin"])
