from flask import render_template  #функция принимает имя шаблона и список переменных аргументов шаблона, а возвращает готовый шаблон с замененными аргументами.
# Под капотом: функция render_template вызывает шаблонизатор Jinja2, который является частью фреймворка Flask. Jinja2 заменяет блоки {{...}} на соответствующие им значения, переданные как аргументы шаблона.
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # выдуманный пользователь
    posts = [ # список выдуманных постов
        { 
            'author': { 'nickname': 'John' }, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)# простое представление, которое просто возвращает строку для отображения в пользовательском браузере. 
#Два декоратора route создают привязку адресов / и /index к этой функции.