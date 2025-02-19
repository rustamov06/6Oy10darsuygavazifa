from django.contrib import admin
from .models import Course, Lesson, Comment, Profile


class Courseadmin(admin.ModelAdmin):
    list_display = ('name', 'photo')
    list_display_links = ('name',)
    search_fields = ('name',)
admin.site.register(Course, Courseadmin)


class Lessonadmin(admin.ModelAdmin):
    list_display = ('lesson_name', 'course', 'date' , 'summary')
    list_display_links = ('lesson_name', )
    search_fields = ('lesson_name', 'course')
    list_max_show_all = 10
    list_per_page = 10
admin.site.register(Lesson, Lessonadmin)



class Commentadmin(admin.ModelAdmin):
    list_display = ('text', 'lesson', 'user', 'created')
    list_display_links = ('text',)
    search_fields = ('user',)
    list_max_show_all = 10
    list_per_page = 10
admin.site.register(Comment, Commentadmin)

class Profileadmin(admin.ModelAdmin):
    list_display = ('user', 'profession')
    list_display_links = ('user',)
    search_fields = ('user',)
    list_max_show_all = 10
    list_per_page = 10
admin.site.register(Profile, Profileadmin)