from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['user1', 'user2']

def sign_up_by_django(request):
    info={}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]
            if password == repeat_password and int(age) >= 18 and username not in users:
                users.append(username)
                return HttpResponse(f'Приветствуем, {username}!')
            else:
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif int(age) < 18:
                    info['error'] = 'Возраст должен быть старше 18 лет'
                else:
                    info['error'] = 'Пользователь  уже существует'
        else:
                info['error'] = 'Некорректные данные'

    else:
        form = UserRegister()
    info['form'] = form
    return render(request,'fifth_task/registration_page.html', {'info':info})


def sign_up_by_html(request):
    info={}
    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        print(f'Username:{username}')
        print(f'password:{password}')
        print(f'repeat_password:{repeat_password}')
        print(f'age:{age}')

        if password == repeat_password and int(age) >= 18 and username not in users:
            users.append(username)
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Возраст должен быть старше 18 лет'
            else:
                info['error'] = 'Пользователь  уже существует'

    return render(request, 'fifth_task/registration_page.html', {'info': info})
