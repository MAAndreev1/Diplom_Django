# Web-приложение для сайта постов

## Необходимые связи:

* asgiref==3.8.1
* Django==5.1.2
* sqlparse==0.5.1
* tzdata==2024.2

## Возможности:

1. Идентификация:
   * Регистрация пользователя с хешированием пароля;
   * Однофакторная аутентификация пользователя;
   * Хранение пользовательской информации в базе данных.
2. Посты:
   * Хранение постов в базе данных;
   * Связь пользователя с постом (один к многим).
3. Стена:
   * Стена (страница с полем размещения всех постов);
4. Профиль пользователя:
   * Создание постов;
   * Удаление постов;
   * Стена (страница с полем размещения своих постов).

## Шаблоны страниц:

* login.html - шаблон страницы авторизации;
* registration.html - шаблон страницы регистрации;
* main_page.html - шаблон главной страницы с постами;
* your_profile.html - шаблон страницы профиля;
* create_post.html - шаблон страницы создания постов.

