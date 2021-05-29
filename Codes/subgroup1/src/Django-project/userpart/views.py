from django.db import reset_queries
from django.shortcuts import render, redirect
from .models import *
from .UserModule import *
from .userclasses import *

# Create your views here.

def signup(request):
    return render(request, 'signup.html')

#success signup
def dosignup(request):
    if request.method == 'POST':
        id = request.POST['id']
        pw = request.POST['pw']
        #new_user = WebUser(user_id=id, user_pw = pw)
        #new_user.save()
    return render(request, 'success.html')
    
def login(request):
    id = request.POST.get('id')
    pw = request.POST.get('pw')

    A = AccountInfo.AccountInfo((id,pw,False,'','','',False))
    UM = UserModule()

    ret = UM.register(A)

    return render(request, 'login.html', {'errMsg' : ret, 'check' : ret})

    '''
    check = 0
    errMsg = ''
    try : 
        if request.session.get('id', False):
            errMsg = request.session.get('id')+'님 반갑습니다'
            check = 1
        elif id == None or pw == None :
            errMsg = 'ID 또는 비밀번호를 입력하지 않았습니다.'
        elif User_info.objects.filter(id = id, pw = pw):
            errMsg = '로그인 성공!'
            check = 1
            request.session['id'] = request.POST.get('id')
            request.session['check'] = check
        else:
            errMsg = '로그인 실패'

    except:
        errMsg = 'ID 또는 비밀번호가 불일치합니다.'

    context = {'errMsg' : errMsg, 'check' : check}

    return render(request, 'login.html', context)
    '''

def main(request):
    
    return render(request, 'main.html')

def free(request):
    return render(request, 'free.html')

def logout(request):
    if request.method == 'POST':
        request.session.modified = True
        #del request.session['id']
        return redirect('home')
    return render(request, 'login.html')

def home(request):
    UC = UserModule()
    print(UC)
    return render(request, 'home.html')
