from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import UNUSABLE_PASSWORD
#from PIL import Image
from sorl.thumbnail import ImageField
import string,random,datetime

def get_photo_storage_path(photo_obj, filename):     
        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
        storage_path = 'img/' + random_string + '_' + filename
        print storage_path
        return storage_path
    
class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True)
    contact_no=models.IntegerField(null=True, blank=True)
    image=models.ImageField(upload_to=get_photo_storage_path)
    
    def __str__(self):
        
        return "%s's profile" % self.user
    
class Post(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    post= models.CharField(max_length=500)
    image=models.ImageField(upload_to=get_photo_storage_path, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    #number_of_reply = models.IntegerField(default=0, null=True, blank=True)
    def __unicode__(self):
        return self.post
    
class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    comment= models.CharField(max_length=500)
    #number_of_reply = models.IntegerField(default=0, null=True, blank=True)
    
    def __unicode__(self):
        return self.comment
