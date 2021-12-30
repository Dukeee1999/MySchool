class Users:
    users=[]

    def __init__(self,user):
        self.user = user

    def appendUser(self):
        self.users.append(self.user)

    def getUsers(self):
        return self.users