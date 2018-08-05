from .forms import FormTask, FormUser, UserLoginForm, FormCompled
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
        cheker.checking_state()
        tasks = Task.objects.filter(owner=request.user).filter(state='activ').order_by('date_finish')
    return render(request, 'taskapp/home.html', {'tasks': tasks})


# страница c проваленными заданиями
def before(request):
    tasks = ''
    if request.user.is_authenticated:
        date = datetime.datetime
        cheker = Checker(request.user)
        cheker.checking()
        cheker.checking_state()
        tasks = Task.objects.filter(owner=request.user).filter(state='fail').filter(
            state='fail').order_by('date_finish')
    return render(request, 'taskapp/before.html', {'tasks': tasks})


# страница с выполнеными задачами
def compled(request):
    tasks = ''
    if request.user.is_authenticated:
        cheker = Checker(request.user)
        cheker.checking()
        cheker.checking_state()
        tasks = Task.objects.filter(owner=request.user).filter(
            state='compl').order_by('date_finish')
    return render(request, 'taskapp/compled.html', {'tasks': tasks})


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
    if request.method == "POST":
        form = FormCompled(request.POST)
        if form.is_valid():
            Task.objects.filter(pk=pk).update(state='compl')
            text_ok = 'Поздравляю с выполненой целью'
            return render(request, 'taskapp/task_detail.html', {'task': task, 'form': form, 'text_ok': text_ok})
    if task.owner != request.user:
        return redirect('home')
    form = FormCompled
    return render(request, 'taskapp/task_detail.html', {'task': task, 'form': form})


def about(request):
    return render(request, 'taskapp/about.html', {})
