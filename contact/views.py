from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from datetime import datetime
from.models import Contact


def contact(request):
    if request.method == 'post':
        name = request.post['name']
        email = request.post['email']
        message = request.post['message']

        contact = Contact(name=name, email=email,
                          message=message, contact_date=datetime.now)

        contact.save()

        send_mail('hello. I am mohammd feili', message,
                  email, ['mfeili1999@gmail.com'])
        messages.success(request, 'Your mail successfully sended!')
        return redirect('index')

    else:
        return render(request, 'contact.html')


def join_us(request):
    if request.method == 'post':
        firstname = request.post['firstname']
        lastname = request.post['lastname']
        username = request.post['username']
        email = request.post['email']
        password1 = request.post['password1']
        password2 = request.post['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is taken')
                return redirect('join-us')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The email is being used')
                    return redirect('join-us')
                else:
                    user = User.objects.create_user(
                        username=username,
                        first_name=firstname,
                        last_name=lastname,
                        email=email,
                        password=password1)

                    #auth.login(request, user)
                    user.save()

                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('index')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('join-us')
    else:
        return render(request, 'register/join-us.html')
