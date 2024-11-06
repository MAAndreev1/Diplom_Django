from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password
import datetime

from django.template.defaultfilters import title

from app.models import *
from app.forms import *

# Create your views here.
def login(request):
    user_list = Users.objects.all()
    form = LoginForm()

    info = {}
    title = 'Авторизация'
    href = '#'
    title_command = 'Войдите в профиль!'
    context = {
        'form': form,
        'info': info,
        'title': title,
        'href': href,
        'title_command': title_command,
    }
    # Если POST
    if request.method == 'POST':
        # Получение и проверка формы
        form = LoginForm(request.POST)
        if form.is_valid():
            # Получение данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Обработка данных формы
            for user in user_list:
                if username == user.username:
                    # Если пользователь существует
                    if check_password(password, user.password):
                        # Если пароли совпадают
                        info.update({'error': 'Вход выполнен успешно!'})
                        request.session['user'] = user.username
                        return redirect('/main_page')
            # Если пароли НЕ совпадают
            info.update({'error': 'Неверный логин или пароль!'})
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)


def registration(request):
    user_list = Users.objects.all()
    form = RegistrationForm()

    info = {}
    title = 'Регистрация'
    href = '/'
    title_command = 'Заполните форму!'
    context = {
        'form': form,
        'info': info,
        'title': title,
        'href': href,
        'title_command': title_command,
    }
    # Если POST
    if request.method == 'POST':
        # Получение и проверка формы
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Получение данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']

            # Обработка данных формы
            if password == repeat_password:
                for user in user_list:
                    if username == user.username:
                        # Если пользователь уже существует
                        info.update({'error': f'Логин {username} занят!'})
                        return render(request, 'registration.html', context)
                # Если пользователь новый
                Users.objects.create(username=username, password=make_password(password))
                info.update({'info': 'Вы зарегистрированы!'})
                return redirect('/')
            else:
                # Если пароли не совпали
                info.update({'error': 'Пароли не совпадают'})
                return render(request, 'registration.html', context)

    # Если GET
    return render(request, 'registration.html', context)


def create_post(request):
    user = request.session.get('user')
    user = Users.objects.get(username=user)
    form = CreatePost()

    info = {}
    title = 'Создание поста'
    href = '/main_page/your_profile/'
    title_command = 'Заполните форму!'
    context = {
        'form': form,
        'info': info,
        'title': title,
        'href': href,
        'title_command': title_command,
    }
    # Если POST
    if request.method == 'POST':
        # Получение и проверка формы
        form = CreatePost(request.POST)
        if form.is_valid():
            # Получение данных формы
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Posts.objects.create(title=title,
                                 description=description,
                                 date_of_creation=datetime.date.today(),
                                 user=user)
            return redirect('/main_page/your_profile/')

    return render(request, 'create_post.html', context)


def main_page(request):
    user = request.session.get('user')
    post_list = []
    for i in Posts.objects.all():
        post_list.append(i)
    post_list.reverse()

    title = 'Главная страница'
    href_main = '#'
    href_prof = 'your_profile/'
    context = {
        'title': title,
        'user': user,
        'href_main': href_main,
        'href_prof': href_prof,
        'post_list': post_list,
    }
    return render(request, 'main_page.html', context)


def your_profile(request):
    user = request.session.get('user')
    user_id = Users.objects.get(username=user).id
    post_list = []
    for i in Posts.objects.filter(user=user_id):
        post_list.append(i)
    post_list.reverse()

    title = 'Ваш профиль'
    href_main = '/main_page'
    href_prof = '#'
    context = {
        'title': title,
        'user': user,
        'href_main': href_main,
        'href_prof': href_prof,
        'post_list': post_list,
    }
    # Если POST
    if request.method == 'POST':
        if 'delete' in request.POST:
            post_id = request.POST['delete']
            Posts.objects.filter(id=post_id).delete()

            post_list = []
            for i in Posts.objects.filter(user=user_id):
                post_list.append(i)
            post_list.reverse()
            context['post_list'] = post_list
            return render(request, 'your_profile.html', context)

    # Если GET
    return render(request, 'your_profile.html', context)