from django.shortcuts import render
from .form import StudentForm, RawStudentForm

# Create your views here.
from .models import Student


def form(request):
    initial_data = {
        'email':'google@gmail.com'
    }
    my_form = StudentForm(request.POST or None, initial=initial_data)
    if my_form.is_valid():
        Student.objects.create(**my_form.cleaned_data)
        # my_form.save()
        # my_form = StudentForm()

    return render(request, "app1/form.html", {'form':my_form})

def form1(request):
    raw_student = RawStudentForm(request.POST or None)
    if raw_student.is_valid():
        Student.objects.create(**raw_student.cleaned_data)
    else:
        raw_student.errors
    return render(request, "app1/form1.html", {'student':raw_student})