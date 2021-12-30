from unittest import TestCase

from pojo.User import User


class TestUser(TestCase):
    def test_get(self):
        user = User(1,"duke","12345")
        print(user.getId())
        print(user.getUserName())
        print(user.getPassWord())

