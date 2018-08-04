from .forms import FormTask, FormUser, UserLoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .models import Task
from django.shortcuts import render, get_object_or_404
import datetime
from .checkdate import Checker

# Create your views here.
# Отображает форму добавления задания
# После успешного добавления форма очищается,выводится сообщение об успехе
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


# Домашняя страница
def home(request):
    tasks = ''
    if request.user.is_authenticated:
        date = datetime.datetime
        cheker = Checker(request.user)
        cheker.checking()
        tasks = Task.objects.filter(owner=request.user).filter(date_finish__gt=date.today()).order_by('date_finish')
    return render(request, 'taskapp/home.html', {'tasks': tasks})


# Страница успешной регистрации
def cong(request):
    return render(request, 'taskapp/congrations_up.html', {})


# Страница регестрации
# При успешной регистрации переходит на страницу с поздравлением
# Далее на главную страницу
def sign_up(request):
    if request.method == "POST":
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.data['username'], password=form.data['password1'])
            login(request, user)
            return redirect('cong')
    else:
        form = FormUser()
    return render(request, 'taskapp/sign_up.html', {'form_sign_up': form})


# Страница для входа
def sign_in(request):
    text_err = 'Не правильный логин или пароль'
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data['username'], password=form.data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form = UserLoginForm
                return render(request, 'taskapp/sign_in.html', {'form': form, 'text_err': text_err})
    form = UserLoginForm
    return render(request, 'taskapp/sign_in.html', {'form': form})


# выход
def sign_out(request):
    logout(request)
    return redirect('home')


# Вывод отдельной задачи
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.owner != request.user:
        return redirect('home')
    return render(request, 'taskapp/task_detail.html', {'task': task})
