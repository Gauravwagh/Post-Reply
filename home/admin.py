from django.contrib import admin
from home.models import Post, Comment, UserProfile


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)


#admin.site.register(Registration)
#admin.site.register(Employee_Details)  # Whatever class we create in model.py we have to register that class in admin.py file

# Register your models here.
