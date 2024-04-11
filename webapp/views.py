import os
from django.conf import settings
from django.shortcuts import redirect, render,HttpResponse
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
        context['username']= username
        context['userType'] = user
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
            return redirect('/index/')
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

def studentmarksResult(request,subject):
    test_name = request.GET.get('test_name')
    sort_order = request.GET.get('sort')
    marks_query = Marks.objects.all()
    student_regno = request.session.get('username')
    marks_query = marks_query.filter(subject=subject,student_regno=student_regno)
    # Filter by test name
    # Apply sorting if test name is provided
    if test_name:
        marks_query = marks_query.filter(test_name=test_name)
    # If test name is not provided, sort all records for the subject
    else:
        if sort_order == 'asc':
            marks_query = marks_query.order_by('marks')
        elif sort_order == 'desc':
            marks_query = marks_query.order_by('-marks')
    unique_tests = Marks.objects.values('test_name').annotate(count=Count('test_name'))
    context =  {}
    context['unique_tests'] = unique_tests
    context['marks'] = marks_query
    context['subject'] = subject
    return render(request,'studentmarks_result.html',context)

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
            marks_query = marks_query.order_by('test_name','marks')
        elif sort_order == 'desc':
            marks_query = marks_query.order_by('test_name','-marks')
    unique_tests = Marks.objects.values('test_name').annotate(count=Count('test_name'))
    context =  {}
    context['unique_tests'] = unique_tests
    context['marks'] = marks_query
    context['subject'] = subject
    return render(request,'teachermarks_result.html',context)

def editMarks(request,id):
    markID = ""
    url = "/"
    br = False
    for char in id:
        if char.isdigit():
            markID += char
        else:
            if char.isupper():
                if(not br):
                    url += '/'
                    br = True
                url += char
            else:
                url += char

    markID = int(markID)
    marks = Marks.objects.get(id=markID)
    marks.marks = request.POST.get('marks')
    marks.save()
    return redirect(url)

def deleteMarks(request,id):
    markID = ""
    url = "/"
    br = False
    for char in id:
        if char.isdigit():
            markID += char
        else:
            if char.isupper():
                if(not br):
                    url += '/'
                    br = True
                url += char
            else:
                url += char

    markID = int(markID)
    marks = Marks.objects.get(id=markID)
    marks.delete()
    return redirect(url)

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

def deleteNote(request,id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('/index/')

def view_pdf(request, pdf_path):

    pdf_path = pdf_path[5:]
    document_path = os.path.join(settings.NOTES_ROOT, str(pdf_path))
    if os.path.exists(document_path):
        with open(document_path, 'rb') as pdf:
            pdf_content = pdf.read()
        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{os.path.basename(document_path)}"'
        return response
    return HttpResponse("Document not found", status=404)


