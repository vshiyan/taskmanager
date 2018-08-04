from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormTask(forms.ModelForm):
    title = forms.CharField(label=(u'Название задачи'), max_length=40,
                            widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    date_finish = forms.DateTimeField(label=(u'Крайний срок исполнения задачи'),
                                      widget=forms.SelectDateWidget(attrs={'class': 'form-control form-control-sm'}))
    descrition = forms.CharField(label=(u'Описание задачи'), max_length=1000,
                                  widget=forms.Textarea(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Task
        fields = ('title', 'date_finish', 'descrition')


class FormUser(UserCreationForm):
    username = forms.CharField(label=(u'Введите имя пользователя'), max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=(u'Введите адрес лектронной почты'),max_length=254,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label=(u'Введите пароль'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=(u'Повторите пароль'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserLoginForm(forms.Form):
    username = forms.CharField(label=(u'Имя пользователя'), max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=(u'Пароль'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
