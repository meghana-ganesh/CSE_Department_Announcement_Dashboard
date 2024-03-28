from django.shortcuts import redirect, render,HttpResponse
from .forms import LoginForm
from .models import User

# Create your views here.
def index(request):
    username = request.session.get('username','')
    user = request.session.get('user','')
    context = {}
    context['userForm'] = LoginForm()
    if username:
        message = f"Username: {username} User Type: {user}"
        context['message']= message
        return render(request,'index.html',context)
    else:
        context['message']= "Not logged in"
        return render(request,'login.html',context)

def login(request):
    userForm = LoginForm()
    context = {}
    context['userForm'] = userForm
    context['message'] = ""
    return render(request,'login.html',context)

def validateLogin(request):
    username = None
    user = None
    context = {}
    context['message'] = "Error Encountered! Please try again!"
    context['userForm'] = LoginForm()
    if request.method == "POST":
        userform = request.POST
        if userform:
            username = userform['username']
            password = userform['password']
            user = userform['user']
            try:
                record = User.objects.get(username = username)
            except:
                context['message'] = "Invalid Credentials"
                return render(request,'login.html',context)
            if(password == record.password and user == record.user):
                context['message'] = f"Login Successful, Welcome {username} as {user}"
                request.session['username'] = username
                request.session['user'] = user
                return render(request,'index.html',context)
            else:
                context['message'] = "Invalid Credentials"
                return render(request,'login.html',context)
        else:
            return render(request,'login.html',context)
    return render(request,'login.html',context)

def logout(request):
    username = request.session.get('username','')
    context = {}
    if username:
        del request.session['username']
        del request.session['user']
        context['message'] = "Logged out Successfully"
        return redirect('/',context)
    context['message'] = "Not Logged In"
    return redirect('/',context)
            

