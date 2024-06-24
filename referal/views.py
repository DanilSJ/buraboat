from django.shortcuts import render, redirect
from users.models import User
import qrcode
from .mail import send_mail
from random import randrange
from .models import ForgotPass
from django.contrib.auth.hashers import make_password, check_password
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

def referal(request):
    if 'users' in request.session:
        data = User.objects.get(id=request.session.get('users'))
        if 'exit' in request.POST:
            del request.session['users']
            return redirect('/login/')

        if 'generate' in request.POST:
            url = f"/referal/ref_param/{data.id}/"

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color="black", back_color="white")


            qr_image.save(f"media/qr/qr_referal_{data.id}.png")

            base_image = Image.open('media/img/ticket.png')

            second_image = Image.open(f'media/qr/qr_referal_{data.id}.png')
            second_image = second_image.resize((838, 838))

            x_position = 1175
            y_position = 1150

            base_image.paste(second_image, (x_position, y_position))
            base_image = base_image.convert('RGB')

            base_image.save(f'media/qr/qr_referal_{data.id}.png')


            context = {
                'qr': f'media/qr/qr_referal_{data.id}.png',
                'id': data.id,
                'data': data,
                'urlRef': url
            }

            return render(request, 'referal/index.html', context=context)

        context = {
            'data': data
        }

        return render(request, 'referal/index.html', context=context)
    else:
        return redirect('/login/')


def referal_ref(request, pk):
    if 'users' in request.session:

        data = User.objects.filter(id=pk)

        for el in data:
            balance = el.balance+1
            referal_people = el.referal_people+1

            data.update(balance=balance, referal_people=referal_people)

        request.session['referal'] = request.session["users"]

        # 1
        print(request.session['referal'])
        return redirect(f"/{os.getenv('MAIN_HOST_PATH_FRONT')}/")
    else:
        data = User.objects.all()
        if 'register' in request.POST:
            for el in data:
                if request.POST['email'] == el.email and request.POST['password'] == el.password:
                    request.session['users'] = el.id
                    return redirect(f'/referal/ref_param/{pk}/')
        return render(request, 'login/index.html')


def register(request):

    if 'register' in request.POST:

        if request.POST['name'] == '' or request.POST['email'] == '' or request.POST['phone'] == '' or request.POST['password'] == '':
            return redirect('/register/')

        data = User.objects.filter(email=request.POST['email']).exists()
        if data:
            return redirect('/register/')

        code = randrange(10000, 99999)
        request.session['success_code'] = {
            'code':code
        }

        user = User.objects.create(
            username=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            password=make_password(request.POST['password']),
        )

        try:
            a123=send_mail(
            subject='Bura Boat confirmation code',
            message=f'Confirmation code: {code}',
            from_email=request.POST['email'],
            recipient_list=[request.POST['email']],
            fail_silently=False,)
        except Exception:
            print(a123)
            
        request.session['users'] = user.id

        return redirect('/referal/')
    return render(request, 'register/index.html')

def success_code(request):
    if 'success' in request.POST:
        try:
            code = int(request.POST['code'])

            if code == request.session.get('success_code')['code']:
                User.objects.update(
                    email_confirmation=True
                )
                return redirect('/login/')
        except Exception:
            pass

    return render(request, 'register/code.html')

def login(request):
    data = User.objects.all()
    if 'enter' in request.POST:
        for el in data:
            print(request.POST['email'])
            print(el.email )
            if request.POST['email'] == el.email and check_password(request.POST['password'], el.password):
                request.session['users'] = el.id
                return redirect('/referal/')
    return render(request, 'login/index.html')

def ForgotPassword(request):
    if 'reset' in request.POST:
        code = randrange(10000, 99999)

        url = request.build_absolute_uri(f"/ForgotPasswordSuccess/{code}/")

        try:
            send_mail(
                subject='Bura Boat reset password',
                message=f'Link: {url}',
                from_email=request.POST['email'],
                recipient_list=[request.POST['email']],
                fail_silently=False
                )
        except Exception:
            pass
        request.session['forgot'] = {
            'email':request.POST['email']
        }


        ForgotPass.objects.create(
            email=request.POST['email'],
            code=code
        )


    return render(request, 'forgot/index.html')

def ForgotPasswordSuccess(request, pk):
    data = ForgotPass.objects.filter(code=pk).exists()
    if data:
        if 'success' in request.POST:
            if request.POST['password'] == '':
                return redirect(f'/ForgotPasswordSuccess/{pk}/')

            User.objects.filter(email=request.session.get('forgot')['email']).update(
                password=request.POST['password']
            )
            ForgotPass.objects.get(code=pk).delete()
            return redirect('/login/')

        return render(request, 'forgot/pass.html')
    else:
        return redirect('/login/')
