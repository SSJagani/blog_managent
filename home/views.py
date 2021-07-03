from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from blog.models import Blog
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Count
from django.contrib.auth import authenticate ,login, logout
# Create your views here.

def index(request):
	if request.session.has_key('username'):
		print(request.session.session_key)
		blog = Blog.objects.annotate(Count('views')).order_by('-views')[:3]
		context = {'allpost':blog, 'udata' : request.session['username']}
		return render(request , "home/home.html" ,context)
	return render(request , "home/home.html")


def about(request):
	return render(request,"home/about.html")


def contact(request):
	messages.success(request, 'Successfuly add you details Our team contect you soon..')
	messages.error(request, 'Document deleted.')
	messages.warning(request, 'Your account expires in three days.')
	if request.method == "POST":
		name= request.POST.get('name','')
		email= request.POST.get('email','')
		phone= request.POST.get('phone','')
		desc= request.POST.get('desc','')
		print(name,email,phone,desc)
		contact=Contact(name=name,email=email,phone=phone,desc=desc)
		contact.save()
		return render(request,"home/contact.html")
	return render(request,"home/contact.html")

def search(request):
	query = request.GET.get("search")
	post = Blog.objects.filter(Q(title__iexact = query) | Q(title__contains = query))
	if post:
		context = {"allpost" : post}
	else:
		context = {"data" : query}
	return render(request,"home/search.html", context)

def login(request):
	if request.method == 'POST':
		l_email = request.POST.get('u_name')
		l_password = request.POST.get('pass')
		print(l_email ,l_password)
		user = auth.authenticate(username = l_email ,password = l_password)
		print(user)
		if user is not None:
			print(user.is_active)
			auth.login(request,user,backend=None)
			request.session['username'] = l_email
			# request.session.set_expiry(100)
			messages.success(request, 'Successfuly Login In Applications...')
			return redirect('Home')
		else:
			messages.error(request , "Invalid Cedantionsal...")
			return redirect('Home')
	else:
		return HttpResponse("404 Error this page..")

def signup(request):
	if request.method == 'POST':
		first_name = request.POST.get('f_name')
		last_name = request.POST.get('l_name')
		user_name = request.POST.get('user_name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		c_password = request.POST.get('c_password')
		print(first_name ,last_name , user_name , email , password , c_password)
		
		## check validation
		if len(user_name) >10:
			messages.warning(request , "UserName Must Be Under 10 Charater.")
			return redirect('Home')

		if not user_name.isalnum():
			messages.warning(request , "User Name must be charter and numrical..")
			return redirect('Home')

		if password != c_password:
			messages.warning(request , "Password Not Match Type Same Password.")
			return redirect('Home')
		else:
			## create User in database 
			myuser = User.objects.create_user(user_name , email , password)
			myuser.first_name = first_name
			myuser.last_name = last_name
			myuser.save()
			messages.success(request, 'Successfuly Create User...')
			return redirect("Home")
	else:
		return HttpResponse("404 Page Not Found..")

def logout(request):
	print(dict(request.session))
	del request.session['username']
	print("logout")
	auth.logout(request)
	messages.success(request, 'Successfuly Logout From Applications...')
	return redirect('Home')

def map(request):
	return render(request,'home/map.html')