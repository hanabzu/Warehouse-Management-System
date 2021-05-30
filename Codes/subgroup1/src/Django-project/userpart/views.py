from django.db import reset_queries
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .UserModule import *
from .userclasses import *
import re

# Create your views here.
def acceptUsers(request):
    tAs = data_TempAccountInfo.objects.all()
    context = {'tAs' : tAs}
    return render(request, 'acceptUsers.html', context)

def viewTempAccountInfo(request, tA_id):
    tA= get_object_or_404(data_TempAccountInfo, pk=tA_id)
    #tempAccount = request.POST.get('accountid')
    #tA = data_TempAccountInfo.objects.get(pk=tempAccount)
    return render(request, 'viewTempAccountInfo.html', {'tA' : tA})

def register(request):
    errMsg = ''
    accountid = request.POST.get('accountid')
    password = request.POST.get('password')
    password_conf = request.POST.get('password_conf')
    position = request.POST.get('position')
    name = request.POST.get('name')
    address = request.POST.get('address')

    # start page
    if accountid==None or password==None or position==None:
        return render(request, 'register.html')

    # check blank spaces
    if accountid=='' or password=='' or password_conf =='' or position==''\
       or name =='' or address=='' :
       errMsg = "You have to fill all blanks"
       return render(request, 'register.html',{'errMsg' : errMsg})

    # check ID
    if len(accountid) < 5:
        errMsg = "ID is too short (least : 5)"
        return render(request, 'register.html',{'errMsg' : errMsg})
    if not accountid.isalnum():
        errMsg = "invalid ID"
        return render(request, 'register.html',{'errMsg' : errMsg})
    tAs = data_TempAccountInfo.objects.all()
    for tA in tAs:
        if accountid == tA.accountid:
            errMsg = "ID is waiting for accepting"
            return render(request, 'register.html',{'errMsg' : errMsg})

    # check password
    if ' ' in password:
        errMsg = "invalid password"
        return render(request, 'register.html',{'errMsg' : errMsg})
    if len(password) < 8:
        errMsg = "password is too short (least : 8)"
        return render(request, 'register.html',{'errMsg' : errMsg})
    if password != password_conf:
        errMsg = "You must type same passwords"
        return render(request, 'register.html',{'errMsg' : errMsg})
    if password == accountid:
        errMsg = "Password and ID must differ"
        return render(request, 'register.html',{'errMsg' : errMsg})


    re_withblank = re.compile('[^ a-zA-Z0-9_]+')

    # check position
    if re_withblank.search(position):
        errMsg = "invalid position"
        return render(request, 'register.html',{'errMsg' : errMsg})

    # check name
    if re_withblank.search(name):
        errMsg = "invalid name"
        return render(request, 'register.html',{'errMsg' : errMsg})

    # check address
    if re_withblank.search(address):
        errMsg = "invalid address"
        return render(request, 'register.html',{'errMsg' : errMsg})

    A = AccountInfo.AccountInfo((accountid,password,False,position,name,address,True))
    UM = UserModule()

    ret = UM.register(A) # true false

    if ret == True:
        tA = data_TempAccountInfo(accountid = A._accountid, password = A._password, position = A._position,\
                            name = A._name, address = A._address)
        tA.save()
    else:
        errMsg = "already registered ID"

    if errMsg=='':
        return render(request, 'success.html')
    else:
        return render(request, 'register.html',{'errMsg' : errMsg})
    

#success signup
def dosignup(request):
    ''' if request.method == 'POST':
        id = request.POST['id']
        pw = request.POST['pw']
        #new_user = WebUser(user_id=id, user_pw = pw)
        #new_user.save()'''
    return render(request, 'success.html')
    
def login(request):
    errMsg =''
    accountid = request.POST.get('accountid')
    password = request.POST.get('password')

    # start page
    if accountid==None or password==None:
        return render(request, 'login.html')
        
    # check ID validity
    if len(accountid) < 5:
        errMsg = "ID is too short (least : 5)"
        return render(request, 'login.html',{'errMsg' : errMsg})
    if not accountid.isalnum():
        errMsg = "invalid ID"
        return render(request, 'login.html',{'errMsg' : errMsg})

    # check password validity
    if ' ' in password:
        errMsg = "invalid password"
        return render(request, 'login.html',{'errMsg' : errMsg})
    if len(password) < 8:
        errMsg = "password is too short (least : 8)"
        return render(request, 'login.html',{'errMsg' : errMsg})

    A = AccountInfo.AccountInfo((accountid,password,False,'','','',False))
    UM = UserModule()

    retAuth = UM.authenticateUser(A)

    # login accept,
    if retAuth == 'Agree':
        return render(request, 'success.html')
    elif retAuth == 'Refuse':
        errMsg = "Wrong password"
        return render(request, 'login.html', {'errMsg' : errMsg})
    else: # NoMatch
        errMsg = "No match ID"
        return render(request, 'login.html', {'errMsg' : errMsg})

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

def progressSuccess(request):
    return render(request, 'progressSuccess.html')

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
