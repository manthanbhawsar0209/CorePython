class LoginException(Exception):
    def __init__(self, message):
        super().__init__(message)

LoginId = "Admin"
LoginPassword = "12345"

try:
    if LoginId == "Admin" and LoginPassword == "1235":
        print("You are successfully logged in")

    else:
        raise LoginException("Invalid username or password")

except Exception as e:
    print("LoginException", e)