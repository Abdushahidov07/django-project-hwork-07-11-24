# views.py
from django.shortcuts import render, redirect
from .models import *
from .forms import UserForm, SkillsForm, ProblemsForm, ApplicationForm

# CRUD CVB User

def user_list_view(request):
    users = User.objects.all()
    return render(request, "alluser.html", {"users": users})

def user_detail_view(request, pk):
    user = User.objects.filter(id=pk).first()
    skills = Skills.objects.filter(user_id=pk)
    return render(request, "detailuser.html", {"user": user, "skills": skills})

def user_create_view(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, "createuser.html", {"form": form})

def user_update_view(request, pk):
    user = User.objects.filter(id=pk).first()
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm(instance=user)
    return render(request, "updateuser.html", {"form": form, "user": user})

def user_delete_view(request, pk):
    user = User.objects.filter(id=pk).first()
    if request.method == "POST":
        user.delete()
        return redirect('home')
    return render(request, "deleteuser.html", {"user": user})


# CRUD CVB Skills

def skills_list_view(request):
    skills = Skills.objects.all()
    return render(request, "skillss.html", {"skills": skills})

def skills_detail_view(request, pk):
    skill = Skills.objects.filter(id=pk).first()
    return render(request, "detailskills.html", {"skill": skill})

def skills_create_view(request):
    if request.method == "POST":
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alluser')
    else:
        form = SkillsForm()
    return render(request, "createskills.html", {"form": form})

def skills_update_view(request, pk):
    skill = Skills.objects.filter(id=pk).first()
    if request.method == "POST":
        form = SkillsForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('alluser')
    else:
        form = SkillsForm(instance=skill)
    return render(request, "updateskills.html", {"form": form, "skill": skill})

def skills_delete_view(request, pk):
    skill = Skills.objects.filter(id=pk).first()
    if request.method == "POST":
        skill.delete()
        return redirect('alluser')
    return render(request, "deleteskills.html", {"skill": skill})


# CRUD CVB Problems

def problems_list_view(request):
    problems = Problems.objects.all()
    return render(request, "home.html", {"problems": problems})

def problems_detail_view(request, pk):
    problem = Problems.objects.filter(id=pk).first()
    applications = Application.objects.filter(problems_id=pk)
    return render(request, "detailproblems.html", {"problem": problem, "applications": applications})

def problems_create_view(request):
    if request.method == "POST":
        form = ProblemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProblemsForm()
    return render(request, "createproblems.html", {"form": form})

def problems_update_view(request, pk):
    problem = Problems.objects.filter(id=pk).first()
    if request.method == "POST":
        form = ProblemsForm(request.POST, request.FILES, instance=problem)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProblemsForm(instance=problem)
    return render(request, "updateproblems.html", {"form": form, "problem": problem})

def problems_delete_view(request, pk):
    problem = Problems.objects.filter(id=pk).first()
    if request.method == "POST":
        problem.delete()
        return redirect('home')
    return render(request, "deleteproblems.html", {"problem": problem})


# CRUD CVB Application

def application_list_view(request):
    applications = Application.objects.all()
    return render(request, "allapplication.html", {"applications": applications})

def application_detail_view(request, pk):
    application = Application.objects.filter(id=pk).first()
    return render(request, "detailapplication.html", {"application": application})

def application_create_view(request, pk):
    problem = Problems.objects.filter(id=pk).first()
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.problems_id = problem
            application.save()
            return redirect('home')
    else:
        form = ApplicationForm()
    return render(request, "createapplication.html", {"form": form})

def application_update_view(request, pk):
    application = Application.objects.filter(id=pk).first()
    if request.method == "POST":
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('allapl')
    else:
        form = ApplicationForm(instance=application)
    return render(request, "updateapplication.html", {"form": form, "application": application})

def application_delete_view(request, pk):
    application = Application.objects.filter(id=pk).first()
    if request.method == "POST":
        application.delete()
        return redirect('allapl')
    return render(request, "deleteapplication.html", {"application": application})


# Category Views

def category_detail_view(request, pk):
    category = Category.objects.filter(id=pk).first()
    problems = Problems.objects.filter(category_id=pk)
    return render(request, "detailcategory.html", {"category": category, "problems": problems})

def category_list_view(request):
    categories = Category.objects.all()
    return render(request, "allcategory.html", {"categorys": categories})
