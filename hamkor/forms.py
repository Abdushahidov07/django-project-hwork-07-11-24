# forms.py
from django import forms
from .models import User, Skills, Problems, Application

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["f_name", "l_name", "username", "age", "email", "phone_number", "profile_pic", "password"]

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ["skill_name", "description", "category_id", "user_id"]

class ProblemsForm(forms.ModelForm):
    class Meta:
        model = Problems
        fields = ["title", "description", "user_id", "category_id", "city_id", "region_id", "street_id", "img", "status"]

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["user_id", "message", "price", "status", "duration"]
