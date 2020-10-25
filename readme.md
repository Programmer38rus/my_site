<h1 align="center">Домашняя работа</h1> 


<h1>D6.11</h1>
<h3>:muscle: Описание проекта:</h3>

<p>Проект библиотеки, в котором можно добавлять авторов и их книги, 
а так же, контролировать кому были одолжены книги.</p>

<h3>:rocket: Инструкция</h3>

<p>Для управления библиотекой зайдите в приложение под Администратором по <a href="http://127.0.0.1:8000/admin">ссылке</a></p>
<p>логин:пароль admin:admin</p>

<h3>Cсылки:</h3>

<b><a href='http://127.0.0.1:8000/friends'>Список друзей из шаблона с применением CSS из статика</a></b>

<b><a href="http://127.0.0.1:8000/base">Ссылка на базовый шаблон с применением extends</a></b>

<a href='http://127.0.0.1:8000/authors'>***Основная страница библиотеки, с картинками***</a>
Хотелось бы обратнуюю связь по реализации. Возник вопрос правильности написания Шаблона. 
В нем я сделал логику "if" для вывода списков книг авторов что было удобно, но не известно 
на сколько это правильно.  

Дайте совет. Хорошо это или стоило реализовать это в <b>views.py</b>




<h1>D5</h1>

Доделал задание по вашим комментариям.

<br>

<a href='http://127.0.0.1:8000/admin/p_library/friend/'>Список друзей из админки</a>



Для установки всех зависимостей используйте из коммандной строки
в дериктории проекта коману.
## Клонирование приложения
<p>Чтобы скопировать приложение себе на компютер введите из консоли команду</p>

```
git clone https://github.com/Programmer38rus/my_site.git
```
перейдите в корневую папку приложения и следуйте дальнейшим инструкциям :)

## Установка зависимостей

```
pip install -r requirements.txt
```

## Запуск из под Windows
```
py manage.py runserver
```

## Запуск из под Unix 
```
python3 manage.py runserver
```
