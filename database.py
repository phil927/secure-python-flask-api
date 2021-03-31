def does_user_exist(username: str) -> bool:
    return False


def register_user(username: str, password_hash: str):
    print(
        "Registering User with Username = "
        + username
        + " and password hash = "
        + password_hash
    )
