from django import forms

# class for name form
class name_form(forms.Form):
    name = forms.CharField()

# class for age form
class age_form(forms.Form):
    age = forms.IntegerField()

# class for email form
class email_form(forms.Form):
    email = forms.EmailField()
