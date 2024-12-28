from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Post
from django.contrib.auth.models import Permission
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import DataModel
@login_required
def index(request):
    posts = Post.objects.all()
    return render(request, 'main/index.html', {'posts': posts})

@permission_required('main.add_post', raise_exception=True)
def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title, content=content, created_by=request.user)
        send_mail('Yangi Post', f'Post "{title}" yaratildi!', 'admin@example.com', ['user@example.com'])
        return redirect('index')
    return render(request, 'main/add_post.html')

@permission_required('main.change_post', raise_exception=True)
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('index')
    return render(request, 'main/edit_post.html', {'post': post})

@permission_required('main.delete_post', raise_exception=True)
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


def index(request):
    return render(request, 'main/index.html')

@login_required
@permission_required('main.add_data', raise_exception=True)
def send_email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        recipient = request.POST['recipient']
        try:
            send_mail(subject, message, 'your_email@gmail.com', [recipient])
            return render(request, 'main/email_sent.html', {'message': 'Email muvaffaqiyatli yuborildi!'})
        except Exception as e:
            return render(request, 'main/email_sent.html', {'message': f'Email yuborishda xatolik: {e}'})
    return render(request, 'main/send_email.html')





@login_required
@permission_required('main.change_datamodel', raise_exception=True)
def update_data(request, data_id):
    data = get_object_or_404(DataModel, id=data_id)

    if request.method == 'POST':
        data.field_name = request.POST['field_name']
        data.save()
        return redirect('index')

    return render(request, 'main/update_data.html', {'data': data})
@login_required
@permission_required('main.add_datamodel', raise_exception=True)
def add_data(request):
    if request.method == 'POST':
        new_data = DataModel.objects.create(field_name=request.POST['field_name'])
        return redirect('index')
    return render(request, 'main/main.add_data.html')
@login_required
@permission_required('main.delete_datamodel', raise_exception=True)
def delete_data(request, data_id):
    data = get_object_or_404(DataModel, id=data_id)
    if request.method == 'POST':
        data.delete()
        return redirect('index')
    return render(request, 'main/delete_data.html', {'data': data})
