dt_data = {
    "userid": 1,
    "username": "user1"
}
class user_Data:
    userid = 1
    username = "user1"
    

    def __init__(self,userid,username):
        self.userid = userid
        self.username = username

usernew = user_Data(**dt_data)
print(usernew.username)
print(usernew.userid)