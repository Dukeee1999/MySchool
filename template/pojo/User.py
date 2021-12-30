

class User:

    imgPath = "img/avatar"

    def __init__(self,id , userName , passWord , email):
        self.id = id
        self.userName = userName
        self.passWord = passWord
        self.email = email

    def getId(self):
        return self.id

    def getUserName(self):
        return self.userName

    def getPassWord(self):
        return self.passWord

    def getEmail(self):
        return self.email