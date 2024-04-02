import re
from django.shortcuts import redirect, render,HttpResponse
from django.urls import is_valid_path
from .forms import LoginForm,AnnouncementsForm,MarksForm,NotesForm
from .models import User,Announcements,Marks,Note
from django.db.models import Count

# Create your views here.
def index(request):
    username = request.session.get('username','')
    user = request.session.get('user','')
    context = {}
    context['userForm'] = LoginForm()
    if username:
        message = f"Username: {username} User Type: {user}"
        context['message']= message
        context['announcements'] = Announcements.objects.all().order_by('-date')
        unique_subjects = Marks.objects.values('subject').annotate(count=Count('subject'))
        context['notes'] = Note.objects.all().order_by('-date')
        context['unique_subjects'] = unique_subjects
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
                return redirect('/index/')
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

def announcementsForm(request):
    return render(request,'announcementsForm.html',{'announcementsForm':AnnouncementsForm})

def addAnnouncements(request):
    if request.method == "POST":
        form = AnnouncementsForm(request.POST)
        if form.is_valid():
            form.save()
            a_obj = Announcements.objects.all().order_by('-date')
            m_obj = Marks.objects.all().order_by('-date')
            return render(request,'index.html',{'announcements':a_obj,'marks':m_obj})
    return redirect('/announcementsForm/')

def deleteAnnouncement(request,id):
    announcement = Announcements.objects.get(id=id)
    announcement.delete()
    return redirect('/index/')

def marksForm(request):
    return render(request,'marksForm.html',{'marksForm':MarksForm})

def addMarks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            a_obj = Announcements.objects.all().order_by('-date')
            m_obj = Marks.objects.all().order_by('-date')
            return redirect('/index/')
    return redirect('/marksForm/')

def studentmarksResult(request):
    m_obj = Marks.objects.all().order_by('-date')
    return render(request,'studentmarks_result.html',{'marks':m_obj})

def teachermarksResult(request,subject):
    test_name = request.GET.get('test_name')
    sort_order = request.GET.get('sort')
    marks_query = Marks.objects.all()
    marks_query = marks_query.filter(subject=subject)
    # Filter by test name
    # Apply sorting if test name is provided
    if test_name:
        marks_query = marks_query.filter(test_name=test_name)
    # If test name is not provided, sort all records for the subject
    else:
        if sort_order == 'asc':
            marks_query = marks_query.order_by('test_name', 'marks')
        elif sort_order == 'desc':
            marks_query = marks_query.order_by('test_name', '-marks')
    unique_tests = Marks.objects.values('test_name').annotate(count=Count('test_name'))
    context =  {}
    context['unique_tests'] = unique_tests
    context['marks'] = marks_query
    context['subject'] = subject
    return render(request,'teachermarks_result.html',context)

def documentForm(request):
    return render(request,'documentForm.html',{'notesForm':NotesForm})

def addNotes(request):
    if request.method == "POST":
        form = NotesForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            context = {
                'message': 'Notes added successfully.',
                'announcements': Announcements.objects.all().order_by('-date'),
                'unique_subjects': Marks.objects.values('subject').annotate(count=Count('subject')),
                'notes': Note.objects.all().order_by('-date'),
            }
            return render(request, 'index.html', context)
        else:
            print(form.errors) 
    return redirect('/documentForm/')


