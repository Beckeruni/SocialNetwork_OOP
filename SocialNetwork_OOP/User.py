from abc import ABCMeta, abstractmethod
import matplotlib
from matplotlib import pyplot as plt
import Post
class Observerable:

    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)
    
    def register(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def unregister_all(self):
        self.observers.clear()
    


class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    
    def update(self, *args):
        '''' Get Notifications'''


class User(IObserver):
    # any new user has username, password
    # also has data - followers and posts
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = set()
        self.following = set()
        self.number_of_posts = 0
        self.number_of_followers = 0


    

    def follow(self, other_user):
        self.followers.add(other_user)
        other_user.following.add(self)
        print(f"{self.username} started following {other_user.username} \n")
        return

    


    def publish_post(self, *args):
        newPost = Post.PostFactory.build_post(self.username, *args)
        for observer in self.observers:
            observer.update(newPost)
        return newPost
        


    def update(type, *args):
        if(type == "Text"):
            User.publish_text(*args)
        if(type == "Image"):
            User.publish_image(*args)
        if(type == "Sale"):
            User.publish_sale(*args)
        raise Exception("Not defined. try again \n")
            
    

    def publish_text(self, *args):
        for line in args:
            print(line)
        print(f"{self.username} published a post: \n")
        


    def publish_image(self, *args):
        plt.show(args)
        print(f"{self.username} posted a picture \n")
        

    def publish_sale(self, *args):
        print(f"{self.username} posted a product for sale: \n")
        print(f"For {args[0]}! {args[1]}, price: {args[2]}, pickup from: {args[3]}")


        

    
























'''
    # set the followers the user has
    def follow(self, other_user):
        if other_user != self:
            other_user.add_follower(self)

    # add followers to user
    def add_follower(self, follower):
        self.followers.add(follower)

    def post(self, content):
        post = TextPost(content, self)
        self.posts.append(post)
        Post.PostFactory.publish_post(post)
        self.notify_followers("User {} posted: {}".format(self.username, content))

    def notify_followers(self, message):
        for follower in self.followers:
            follower.update(message)

    def update(self, action):
        print("Notification for {}: {}".format(self.username, action))
'''