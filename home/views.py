from django.shortcuts import render
from django.shortcuts import render_to_response,HttpResponse
from django.template.loader import render_to_string
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
import json
from rest_framework import serializers
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


from home.models import Post, Comment
from home.forms import PostForm, CommentForm, UserProfileForm


def user_register(request):
    if (request.method=="POST"):
        postform = PostForm(request.POST, request.FILES)
        #print postform
        user_name = request.user   
        postform.user = user_name
        
        if postform.is_valid():
            
            profile = postform.save(commit=False)
            print profile.post
            
            profile.user = request.user
            profile.time=timezone.now() 
            #print profile.user        
            profile.save()
            messages.success(request, 'Your post submitted Successfully')
    else:                    
        postform = PostForm()
    return render(request, "home/post.html", { 'postform' : postform })

def Display_post(request):
    if request.method=="GET":
        post = Post.objects.all().order_by('-time')
        #print post
        data = []
        for pos in post:
            rep = Comment.objects.filter(post=pos)
            pos.rep=rep
        html = render_to_string('home/post_reply.html',{"post":post})
        return HttpResponse(html, mimetype="application/json")

@csrf_exempt    
def save_reply(request, id):
    print "in save_reply view"
    if (request.method=="POST"):
        post = Post.objects.get(id=id)
        print request.POST
        print request.user
        rep= request.POST['reply']
        reply = Comment(user=request.user, post=post, comment=rep)
        print reply
        reply.save()
        
        data = {"message":"Reply saved successfully"}
        response = json.dumps(data)
        return HttpResponse(response, mimetype="application/json")

'''    
def Display_post(request):
    if request.method=="GET":
        post = Post.objects.all()
        #print post
        data = []
        for pos in post:
            postdata = pos.post
            userdata = pos.user.username
            postimage = pos.image
            #print type(postimage)
            img = postimage.name
            idpk = pos.pk
            
            record = {"postdata":postdata, "userdata":userdata, "postimage":postimage.url, "idpk":idpk}
            data.append(record)
        response = json.dumps(data,cls=DjangoJSONEncoder)
        return HttpResponse(response, mimetype="application/json")'''