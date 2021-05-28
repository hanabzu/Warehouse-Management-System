from django.shortcuts import render, redirect
from .models import User_info

# Create your views here.

def signup(request):
    return render(request, 'signup.html')

    
def login(request):
    id = request.POST.get('id')
    pw = request.POST.get('pw')
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

def main(request):
    return render(request, 'main.html')

def free(request):
    return render(request, 'free.html')
def logout(request):
    request.session.modified = True
    del request.session['id']
    return redirect('login')

def home(request):

    return render(request, 'home.html')
