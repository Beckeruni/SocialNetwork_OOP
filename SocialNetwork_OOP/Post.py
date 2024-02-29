# Factory design pattern

from abc import ABCMeta, abstractclassmethod


class IPost(metaclass=ABCMeta):
    def publish_post():
        '''Interface Method'''
    
    def like(this, other_user):
        this.num

        
    
    def comment():
        '''Interface Method'''



class Text(IPost):
    def __init__(self, name, type, actual_text):
        self.username = name
        self.type = type
        self.actual_text = actual_text
        self.num_of_likes = 0
        self.liked_by = set()

    
    def like(self, other_user):
        self.num_of_likes +=1
        self.liked_by.add(other_user)
        print(f"notification to {self.username}: {other_user.username} liked your post")

    
    def comment(self, other_user, text):
        print(f"notification to {self.username}: {other_user.username} commented on your post: {text}")
        
        
    

class Image(IPost):
    pass
    







class Sale(IPost):
    def discount(discount_price, password):
        pass





class PostFactory:
    @staticmethod
    def build_post(creator_username, *args):
        if (args[0] == "Text"):
            return Text(creator_username, args[0], args[1])
        if (args[0] == "Image"):
            return Image()
        if (args[0]== "Text"):
            return Sale()
        








'''










class PostFactory:
    def publish_post(self, post_type, *args, **kwargs):
        if post_type == "text":
            return TextPost(*args, **kwargs)
        elif post_type == "image":
            return ImagePost(*args, **kwargs)
        elif post_type == "sale":
            return SalePost(*args, **kwargs)
        else:
            raise ValueError("Invalid post type")


class Post:
    def __init__(self, content, user):
        self.content = content
        self.user = user
        self.likes = set()
        self.comments = []

    def like(self, user):
        self.likes.add(user)
        user.update("Liked your post: {}".format(self.content))

    def comment(self, user, text):
        comment = "{}: {}".format(user.username, text)
        self.comments.append(comment)
        user.update("Commented on your post: {}".format(self.content))


class TextPost(Post):
    pass


class ImagePost(Post):
    def __init__(self, content, user, image_path):
        super().__init__(content, user)
        self.image_path = image_path

    def display(self):
        print("Displaying image from {}".format(self.image_path))


class SalePost(Post):
    def __init__(self, content, user, description, price, location):
        super().__init__(content, user)
        self.description = description
        self.price = price
        self.location = location
        self.sold = False

    def discount(self, percentage):
        self.price *= (100 - percentage) / 100

    def sold(self):
        self.sold = True

    def display(self):
        print("Sale Post: {} - ${} - Location: {}".format(self.description, self.price, self.location))

        '''