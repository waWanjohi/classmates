from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from student.models import Student
from .forms import StudentForm
from django.contrib import messages

def student(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Student added succesfully')
			return redirect('/')

	else:
		form = StudentForm()

	return render(request, 'index.html', {'form':form})


def show(request):
	students = Student.objects.all().order_by('sgender')
	return render(request, "show.html", {'students':students})



# Perform a search
# def search(request):
# 	if request.method == 'GET':
# 		gid = SearchForm(request.GET)
# 		search = print(gid.sname)
# 		results = Student.objects.all().filter(sname__startswith=search)
# 		return redirect('result.html', {'results':results})


# Create a new student model
def add(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Student entry has been created succesfully!")
			return redirect('/')
	else:
		form = StudentForm()

	return render(request, 'add.html', {'form':form})


# delete a student record
def destroy(request, sid):
	child = Student.objects.all()
	student = Student.objects.get(sid=sid)
	student.delete()
	messages.warning(request, "Removed " + student.sname + " from the class list")
	return redirect("/")


# Edit a students form
def edit(request, sid):
	student = Student.objects.get(sid=sid)
	return render(request, 'edit.html', {'student':student}) 



# Update student details after editing
def update(request, sid):
    student = Student.objects.get(sid=sid)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "show.html", {'student': student})



# Enable searching for student
class StudentsSearchListView(ListView):
    model = Student
    template_name = 'result.html'

    def get_queryset(self):
    	query =self.request.GET.get('q')
    	return Student.objects.all().filter(
    		Q(sname__icontains=query) | Q(srow__icontains=query) | Q(sgender__icontains=query) |Q(sid__icontains=query)
    		).order_by('sname')
    	result = query
    	return object_list



# Sort the students by gender
class GenderView(ListView):
	template_name = 'result.html'

	def get_queryset(self):
		query = self.request.GET.get('q')
		return Student.objects.all().filter(
    		Q(sgender__icontains=query)
    		).order_by('sname')

# Show a list of all the students [ordered alphabetically]
def all(request):
	object_list = Student.objects.all().order_by('sname')
	return render(request, 'all.html', {'object_list':object_list})


class HelpView(TemplateView):
	template_name = 'help.html'