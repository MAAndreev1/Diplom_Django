from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password
import datetime

from app.models import *
from app.forms import *

# Create your views here.
def login(request):
    """
        Данная функция является представлением для страницы авторизации.
        Она обрабатывает GET и POST запросы.
        GET - возвращает шаблон страницы авторизации.
        POST - проверяет отправленные на авторизацию данные пользователя с базой данных.
    """
    user_list = Users.objects.all()
    form = LoginForm()

    info = {}
    title_name = 'Авторизация'
    href = '#'
    title_command = 'Войдите в профиль!'
    context = {
        'form': form,
        'info': info,
        'title': title_name,
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
    """
        Данная функция является представлением для страницы регистрации.
        Она обрабатывает GET и POST запросы.
        GET - возвращает шаблон страницы регистрации.
        POST - проверяет отправленные на регистрацию данные пользователя на корректность.
    """
    user_list = Users.objects.all()
    form = RegistrationForm()

    info = {}
    title_name = 'Регистрация'
    href = '/'
    title_command = 'Заполните форму!'
    context = {
        'form': form,
        'info': info,
        'title': title_name,
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
    """
        Данная функция является представлением для страницы создания постов.
        Она обрабатывает GET и POST запросы.
        GET - возвращает шаблон страницы создания постов.
        POST - использует отправленные данные для создания постов.
    """
    user = request.session.get('user')
    user = Users.objects.get(username=user)
    form = CreatePost()

    info = {}
    title_name = 'Создание поста'
    href = '/main_page/your_profile/'
    title_command = 'Заполните форму!'
    context = {
        'form': form,
        'info': info,
        'title': title_name,
        'href': href,
        'title_command': title_command,
    }
    # Если POST
    if request.method == 'POST':
        # Получение и проверка формы
        form = CreatePost(request.POST)
        if form.is_valid():
            # Получение данных формы
            title_name = form.cleaned_data['title']
            description = form.cleaned_data['description']
            Posts.objects.create(title=title_name,
                                 description=description,
                                 date_of_creation=datetime.date.today(),
                                 user=user)
            return redirect('/main_page/your_profile/')

    return render(request, 'create_post.html', context)


def main_page(request):
    """
        Данная функция является представлением для главной страницы с постами.
        Она обрабатывает GET запрос.
        GET - возвращает шаблон главной страницы.
    """
    user = request.session.get('user')
    post_list = []
    for i in Posts.objects.all():
        post_list.append(i)
    post_list.reverse()

    title_name = 'Главная страница'
    href_main = '#'
    href_prof = 'your_profile/'
    context = {
        'title': title_name,
        'user': user,
        'href_main': href_main,
        'href_prof': href_prof,
        'post_list': post_list,
    }
    return render(request, 'main_page.html', context)


def your_profile(request):
    """
        Данная функция является представлением для страницы профиля.
        Она обрабатывает GET и POST запросы.
        GET - возвращает шаблон страницы профиля.
        POST - используется для удаления постов (получает id поста из POST запроса).
    """
    user = request.session.get('user')
    user_id = Users.objects.get(username=user).id
    post_list = []
    for i in Posts.objects.filter(user=user_id):
        post_list.append(i)
    post_list.reverse()

    title_name = 'Ваш профиль'
    href_main = '/main_page'
    href_prof = '#'
    context = {
        'title': title_name,
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