import string
from abc import ABCMeta, abstractstaticmethod
import SocialNetwork
import User
import Post

#singlton design pattern
class ISocialNetwork(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_name():
        """implement in child class"""




class SocialNetwork(ISocialNetwork):
    __instance = None
    tuple_of_user_and_password = []
    users_logged_in = set()

    @staticmethod
    def get_name():
        if SocialNetwork.__instance == None:
            return None
        return SocialNetwork.__instance.name

    def __init__(self, name):
        if(SocialNetwork.__instance != None):
            raise Exception("Already have a network")
        self.name = name
        SocialNetwork.__instance = self


    @staticmethod
    def print_success():
        print(f"The social network {SocialNetwork.get_name} was created!")

    @staticmethod
    def sign_up(username, password):
        if(SocialNetwork.password_used(password) or len(password)>9 or len(password)<3):
            raise Exception("This Password is not secure, try another ")
        new_user = User.User(username, password)
        return new_user
    
    @staticmethod
    def password_used(password):
        for info in range(len(SocialNetwork.tuple_of_user_and_password)):
            if(info[1] == password):
                return True
        return False
    

    @staticmethod
    def log_in(username, password):
        info = (username, password)
        if (info in SocialNetwork.tuple_of_user_and_password):
            print(f"{username} connected")
            SocialNetwork.users_logged_in.add(username)
        
    def log_out(username):
        print(f"{username} disconnected")
        SocialNetwork.users_logged_in.remove(username)

   
    
'''

    def log_in(self, name, password):
        if name in self.users:
            self.net_log = True

    def log_out(self, name):
        self.net_log = True

    def sigh_in(self, name, password):
        if name not in self.users:
            if 4 <= password <= 8:
                self.add_user(name)

    # add all the users of this network
    def add_user(self, user):
        self.users.append(user)

    # add all the posts of this network
    def add_post(self, post):
        SocialNetwork.User.User.post(post)


def display_notifications(self, user):
    # Display notifications for the given user
    for notification in user.notifications:
        print(notification)
'''