# Web-приложение для сайта постов

## Необходимые связи:

* asgiref==3.8.1
* Django==5.1.2
* sqlparse==0.5.1
* tzdata==2024.2
  
![requirements](https://github.com/user-attachments/assets/f7c24ad3-92e2-4e13-b9bf-635935f616d9)

## Возможности:

### 1. Идентификация:
   * Регистрация пользователя с хешированием пароля;
     
   ![image](https://github.com/user-attachments/assets/f88c6c64-e073-4d4d-857c-d3f5a827dbc5)

   * Однофакторная аутентификация пользователя;
  
   ![image](https://github.com/user-attachments/assets/cf01b59f-1cdf-4ea7-8e58-79e884601ba2)

   * Хранение пользовательской информации в базе данных.

   ![image](https://github.com/user-attachments/assets/15c7ba17-5485-4b78-b005-c63488761632)

   
### 2. Посты:
   * Хранение постов в базе данных;
  
   ![image](https://github.com/user-attachments/assets/046eeb2d-85dd-4775-b2bd-43a2bf9cfda3)

   * Связь пользователя с постом (один к многим).
### 3. Стена:
   * Стена (страница с полем размещения всех постов);

   ![image](https://github.com/user-attachments/assets/58a57ef2-62f5-4ca1-8eb3-842f13287094)

### 4. Профиль пользователя:
   * Создание постов;

   ![image](https://github.com/user-attachments/assets/d9646bb9-2828-4824-83ab-0a5cf49bc04a)

   * Удаление постов;
   * Стена (страница с полем размещения своих постов).

   ![image](https://github.com/user-attachments/assets/70c8b3c3-b3b8-4c57-b287-cfe0b070d197)

## Шаблоны страниц:

* login.html - шаблон страницы авторизации;
* registration.html - шаблон страницы регистрации;
* main_page.html - шаблон главной страницы с постами;
* your_profile.html - шаблон страницы профиля;
* create_post.html - шаблон страницы создания постов.

