from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister
from django.template.exceptions import TemplateDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Buyer, Game

def third_task(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы


    link1 = 'Главная task1'
    link2 = 'Магазин task1'
    link3 = 'Корзина task1'
    link4 = 'Регистрация task1'


    context = {
        'link1':link1,
        'link2':link2,
        'link3':link3,
        'link4':link4,
    }
    # возвращает функцию render, импортированную по умолчанию в django
    return render(request, 'third_task.html', context)


def index(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы




    link1 = 'Главная task1'
    link2 = 'Магазин task1'
    link3 = 'Корзина task1'
    link4 = 'Регистрация task1'
    list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']

    games = Game.objects.all()

    context = {
        'link1': link1,
        'link2': link2,
        'link3': link3,
        'link4': link4,
        'list': list,
        'games': games,
    }

    # возвращает функцию render, импортированную по умолчанию в django
    return render(request, 'index.html', context)

def index1(request):

    link1 = 'Главная task1'
    link2 = 'Магазин task1'
    link3 = 'Корзина task1'
    link4 = 'Регистрация task1'


    context = {
        'link1': link1,
        'link2': link2,
        'link3': link3,
        'link4': link4,
    }
    # Напишем переменную, передающую имя второй страницы:
    return render(request, 'index1.html', context)

def menu(request):
    link1 = 'Главная task1'
    link2 = 'Магазин task1'
    link3 = 'Корзина task1'
    link4 = 'Регистрация task1'
    list = ['Atomic Heart task1', 'Cyberpunk 2077 task1', 'PayDay 2 task1']


    context = {
        'link1': link1,
        'link2': link2,
        'link3': link3,
        'link4': link4,
        'list': list,
    }


    # Напишем переменную, передающую имя второй страницы:
    return render(request, 'menu.html', context)



def sign_up_by_django(request):
    # users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        print("Данные, полученные из формы:", request.POST)
        if form.is_valid():
            print("Форма валидна!")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            print(f"Username: {username}, Age: {age}")

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                print("Пароли не совпадают")

            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
                print("Возраст меньше 18 лет")
            # elif username in users:
            #     info['error'] = 'Пользователь уже существует'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
                print("Пользователь уже существует")
            # else:
            #     info['message'] = f'Приветствуем, {username}!'
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                info['message'] = f'Приветствуем, {username}!'
                return redirect('index')
                print(f"Регистрация прошла успешно: {username}")

        else:
            print("Форма невалидна, ошибки:", form.errors)

        info['form'] = form
    else:
        info['form'] = UserRegister()
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    # users = ['user1', 'user2', 'user3']
    info = {}
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = int(request.POST.get('age'))  # Преобразование в целое число

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'

            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=0, age=age)
                info['message'] = f'Приветствуем, {username}!'
                return redirect('index')
            # elif username in users:
            #     info['error'] = 'Пользователь уже существует'
            # else:
            #     info['message'] = f'Приветствуем, {username}!'
        return render(request, 'fifth_task/registration_page.html', info)
    except TemplateDoesNotExist as e:
        print(e)
        print(e.args)
        raise e

#
# def game_list(request):
#     games = Game.objects.all()
#     return render(request, 'game_list.html', {'games': games})




# from django.shortcuts import render
# from django.views.generic import TemplateView
# from .forms import UserRegister
# from django.template.exceptions import TemplateDoesNotExist
#
# def third_task(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы
#
#
#     link1 = 'Главная task1'
#     link2 = 'Магазин task1'
#     link3 = 'Корзина task1'
#
#
#
#     context = {
#         'link1':link1,
#         'link2':link2,
#         'link3':link3,
#     }
#     # возвращает функцию render, импортированную по умолчанию в django
#     return render(request, 'third_task.html', context)
#
#
# def index(request):  # По умолчанию все функции принимают запрос от польз-ля на получение информации и страницы
#
#     link1 = 'Главная task1'
#     link2 = 'Магазин task1'
#     link3 = 'Корзина task1'
#     list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
#
#     context = {
#         'link1': link1,
#         'link2': link2,
#         'link3': link3,
#         'list': list,
#     }
#
#     # возвращает функцию render, импортированную по умолчанию в django
#     return render(request, 'index.html', context)
#
# def index1(request):
#
#     link1 = 'Главная task1'
#     link2 = 'Магазин task1'
#     link3 = 'Корзина task1'
#
#
#     context = {
#         'link1': link1,
#         'link2': link2,
#         'link3': link3,
#     }
#     # Напишем переменную, передающую имя второй страницы:
#     return render(request, 'index1.html', context)
#
# def menu(request):
#     link1 = 'Главная task1'
#     link2 = 'Магазин task1'
#     link3 = 'Корзина task1'
#     list = ['Atomic Heart task1', 'Cyberpunk 2077 task1', 'PayDay 2 task1']
#
#     context = {
#         'link1': link1,
#         'link2': link2,
#         'link3': link3,
#         'list': list,
#     }
#     # Напишем переменную, передающую имя второй страницы:
#     return render(request, 'menu.html', context)
#
#
#
# def sign_up_by_django(request):
#     users = ['user1', 'user2', 'user3']
#     info = {}
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         print("Данные, полученные из формы:", request.POST)
#         if form.is_valid():
#             print("Форма валидна!")
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#             print(f"Username: {username}, Age: {age}")
#
#             if password != repeat_password:
#                 info['error'] = 'Пароли не совпадают'
#                 print("Пароли не совпадают")
#
#             elif age < 18:
#                 info['error'] = 'Вы должны быть старше 18'
#                 print("Возраст меньше 18 лет")
#             elif username in users:
#                 info['error'] = 'Пользователь уже существует'
#                 print("Пользователь уже существует")
#             else:
#                 info['message'] = f'Приветствуем, {username}!'
#                 print(f"Регистрация прошла успешно: {username}")
#
#         else:
#             print("Форма невалидна, ошибки:", form.errors)
#
#         info['form'] = form
#     else:
#         info['form'] = UserRegister()
#     return render(request, 'fifth_task/registration_page.html', info)
#
# def sign_up_by_html(request):
#     users = ['user1', 'user2', 'user3']
#     info = {}
#     try:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             repeat_password = request.POST.get('repeat_password')
#             age = int(request.POST.get('age'))  # Преобразование в целое число
#
#             if password != repeat_password:
#                 info['error'] = 'Пароли не совпадают'
#             elif age < 18:
#                 info['error'] = 'Вы должны быть старше 18'
#             elif username in users:
#                 info['error'] = 'Пользователь уже существует'
#             else:
#                 info['message'] = f'Приветствуем, {username}!'
#         return render(request, 'fifth_task/registration_page.html', info)
#     except TemplateDoesNotExist as e:
#         print(e)
#         print(e.args)
#         raise e