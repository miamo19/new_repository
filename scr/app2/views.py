from django.shortcuts import render
from .form2 import RawTeacherForm

# Create your views here.
from .models import Teacher


def form2(request):
    my_form = RawTeacherForm(request.POST or None)
    if my_form.is_valid():
        Teacher.objects.create(**my_form.cleaned_data)
    else:
        my_form.errors
    """same
    my_form = RawTeacherForm()
    if request.method == "POST":
        my_form = RawTeacherForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Teacher.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    """
    context = {
        "form":my_form,
    }

    return render(request, "app2/form2.html", context)