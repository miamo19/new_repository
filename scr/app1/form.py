from django import forms
from .models import Student

class StudentForm(forms.Form):
    first_name = forms.CharField(label='Name',
                                 widget=forms.TextInput(attrs={"placeholder": "your first name"}))
    email      = forms.EmailField()
    last_name  = forms.CharField(label="Sur-name",
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Your lastname',
                                    "class": "new-class-name two"
                                }))
    gender   = forms.CharField(label="Gender", widget=forms.TextInput(attrs={"placeholder":"Enter you gender"}))
    class Meta:
         model = Student
         fields = "__all__"

    def clean_last_name(self, *args, **kwargs):
        last_name = self.cleaned_data.get("last_name").upper()
        if "CFE" in last_name:
            return last_name
        else:
            raise forms.ValidationError("This is not a valid name")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError('This is not a valid email')
        return email




class RawStudentForm(forms.Form):
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={"placeholder":"your first name"}))
    last_name = forms.CharField(label="",
                                widget=forms.TextInput(attrs={
                                    'placeholder':'Your lastname',
                                    "class":"new-class-name two"
                                }))