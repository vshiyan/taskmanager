from django.shortcuts import render
from .forms import FormTask, FormUser
from django.shortcuts import redirect


# Create your views here.
def add(request):
    if request.method == "POST":
        form = FormTask(request.POST)
        text_ok = 'Задача добавлена'
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            form = FormTask()
            return render(request, 'taskapp/add.html', {'form_task': form, 'text_ok': text_ok})
    else:
        form = FormTask()
    return render(request, 'taskapp/add.html', {'form_task': form})


def home(request):
    return render(request, 'taskapp/home.html', {})


def cong(request):
    return render(request, 'taskapp/congrations_up.html', {})


def sign_up(request):
    if request.method == "POST":
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cong')
    else:
        form = FormUser()
    return render(request, 'taskapp/sign_up.html', {'form_sign_up': form})
