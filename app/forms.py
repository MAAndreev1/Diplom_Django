from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Введите логин')
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput())


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Введите логин')
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput())
    repeat_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput())


class CreatePost(forms.Form):
    title = forms.CharField(label='Введите заголовок')
    description = forms.CharField(label='Напишите пост', widget=forms.Textarea())
