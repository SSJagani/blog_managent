from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Blog,BlogComment
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.

def index(request):
	blog = Blog.objects.all()
	if request.session.has_key('username'):
		context = {"allpost":blog , 'udata' : request.session['username']}
		return render(request , "blog/blog.html" , context)
	context = {"allpost":blog}
	return render(request , "blog/blog.html" , context)

def blogpost(request,slug):
	if request.session.has_key('username'):
		post = Blog.objects.filter(slug=slug).first()
		post.views = post.views + 1
		post.save() 
		comment = BlogComment.objects.filter(post=post,parent=None)
		reply_comment = BlogComment.objects.filter(post=post).exclude(parent=None)
		replyDict = {}
		for reply in reply_comment:
			if reply.parent.sr_no not in replyDict.keys():
				replyDict[reply.parent.sr_no] =[reply]
			else:
				replyDict[reply.parent.sr_no].append(reply)
		print(replyDict)
		context = { "post" :post , "comments" : comment ,"reply_comment":replyDict, 'udata' : request.session['username']}
		return render(request , "blog/blogpost.html", context)
	else:
		post = Blog.objects.filter(slug=slug).first()
		post.views = post.views + 1
		post.save() 
		comment = BlogComment.objects.filter(post=post,parent=None)
		reply_comment = BlogComment.objects.filter(post=post).exclude(parent=None)
		replyDict = {}
		for reply in reply_comment:
			if reply.parent.sr_no not in replyDict.keys():
				replyDict[reply.parent.sr_no] =[reply]
			else:
				replyDict[reply.parent.sr_no].append(reply)
		print(replyDict)
		context = { "post" :post , "comments" : comment ,"reply_comment":replyDict}
		return render(request , "blog/blogpost.html", context)



def blogComment(request):
	print("hello")
	if request.method == 'POST':
		comment= request.POST['comment']
		user= request.user
		post_srno = request.POST['post_srno']
		post= Blog.objects.get(post_id=post_srno)
		parentSrno = request.POST["comment_srno"]
		print(comment,user,post, parentSrno)
		if parentSrno == "":
			comment=BlogComment(comment=comment,user=user,post=post)
			comment.save()
			messages.success(request, 'Successfuly Add Your comment...')
		else:
			parent = BlogComment.objects.get(sr_no = parentSrno)
			comment=BlogComment(comment=comment,user=user,post=post,parent=parent)
			comment.save()
			messages.success(request, 'Successfuly Add Your Reply..')
		return redirect(f'/blog/{post.slug}')
