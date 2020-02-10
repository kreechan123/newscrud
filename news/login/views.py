from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from news.models import Category, Newsinfo, Newsimage
from .forms import addnewsForm

def indexView(request):
	list = Newsinfo.objects.all()
	newslist = {"object_list": list}
	return render(request,'index.html', newslist)

@login_required(login_url='/login/')

def dashboardView(request):
	return render(request,'dashboard.html')

def registerView(request):
	form = "string"
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_url')
		else:
			form = UserCreationForm()

	return render(request,'registration/register.html', {'form':form})

def loginView(request):
	return render(request,'registration/login.html')

def addView(request):
	# q = Category.objects.all()
	# # if request.method == "POST":
	# obj = Category(name="smileyz")
	
	# if q.filter(name=obj.name).exists():
	# 	return redirect('../../')
	# else:
	# 	obj.save()
	# 	return redirect('../../')
	q = Category.objects.all()
	form = "string"
	if request.method == 'POST':
		form = addnewsForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			# pub_date = form.cleaned_data['pub_date']
			p = Newsinfo(title=title, content=content)
			p.save()
	else:
		form = addnewsForm()

	return render(request,'create.html', {"form": form})

def editView(request, id):
	q = Category.objects.all()
	obj = Category(name="smileyz")
	obj.save()
	context = {"object": obj}
	return render(request,'edit.html', context)

def deleteView(request, id):
	obj = get_object_or_404(Newsinfo, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {"object": obj}
	return render(request,'delete.html', context)

