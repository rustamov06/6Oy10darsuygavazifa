from django.urls import path
from .views import index, course_detail, lesson_detail, user_login, user_register, user_logout, profile

urlpatterns = [
    path('', index, name='index'),

    path('course_detail/<int:course_id>', course_detail, name="course_detail"),
    path('lesson_detail/<int:lesson_id>', lesson_detail, name='lesson_detail'),

    path('user_login/', user_login, name='user_login'),
    path('user_register/', user_register, name='user_register'),
    path('user_logout/', user_logout, name='user_logout'),

    path('profile/', profile, name='profile')

]