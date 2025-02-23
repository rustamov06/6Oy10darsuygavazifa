from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Comment, Profile
from .form import CommentFrom, LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User


def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'index.html', context)


@permission_required('main/view_course', raise_exception=True)
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course)
    context = {
        'course': course,
        'lessons': lessons
    }
    return render(request, 'course_detail.html', context)


@permission_required('main.view_lesson', raise_exception=True)
def lesson_detail(request, lesson_id):
    """Dars sahifasini ko‘rsatish va kommentlarni boshqarish"""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    comments = Comment.objects.filter(lesson=lesson)
    form = CommentFrom()

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "create":
            form = CommentFrom(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.lesson = lesson
                comment.user = request.user
                comment.save()
            return redirect("lesson_detail", lesson_id=lesson.id)

        elif action == "update":
            comment_id = request.POST.get("comment_id")
            comment = get_object_or_404(Comment, id=comment_id, lesson=lesson)

            if request.user == comment.user:
                comment.text = request.POST.get("text")
                comment.save()

            return redirect("lesson_detail", lesson_id=lesson.id)

        elif action == "delete":
            comment_id = request.POST.get("comment_id")
            comment = get_object_or_404(Comment, id=comment_id, lesson=lesson)

            if request.user == comment.user:
                comment.delete()

            return redirect("lesson_detail", lesson_id=lesson.id)

    context = {
        "lesson": lesson,
        "comments": comments,
        "form": form
    }
    return render(request, "lesson_detail.html", context)



def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Xush kelibsiz {user.first_name} {user.last_name}")
            return redirect('index')
    else:
        form = LoginForm()
    context = {
        'form' : form
    }

    return render(request, 'user_login.html', context)

def user_register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"{user.username} muofiqiyatli qo'shildi !\n"
                                      "Iltimos login qiling !")
            return redirect("user_login")

    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
@login_required
def user_logout(request):
    logout(request)
    messages.warning(request, f"Siz akoutni tark etingiz janob !")
    return redirect("user_login")



def profile(request, username):

        context = {}
        try:
            user = get_object_or_404(User, username=username)
            lesson = Lesson.objects.filter(author=user)
            profile = get_object_or_404(Profile, user=user)
            context['profile'] = profile
            context['lesson'] = lesson
        except Exception as e:
            messages.error(request, f"{e}")
            return redirect('home')
        return render(request, "profile.html", context)
