from django.shortcuts import render,redirect
from myapp.models import task
from myapp.forms import taskForm

def display(request):
	s=task.objects.all()
	d={'stud':s}
	return render(request,'myapp/index.html',d)

def insert_view(request):
	f=taskForm()
	if request.method=="POST":
		f=taskForm(request.POST)
		if f.is_valid():
			f.save(commit=True)
		return redirect('/')
	d={'form':f}
	return render(request,'myapp/insert.html',d)

def update_view(request,id):
	s=task.objects.get(id=id)
	f=taskForm()
	if request.method=="POST":
		f=taskForm(request.POST,instance=s)
		if f.is_valid():
			f.save(commit=True)
		return redirect('/')
	d={'stud':s}
	return render(request,'myapp/update.html',d)

def delete_view(request,id):
	s=task.objects.get(id=id)
	s.delete()
	return redirect('/')
