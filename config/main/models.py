from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_NULL
from django.core.validators import FileExtensionValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="user/profile", null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    site = models.URLField(null=True, blank=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
         return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=500, verbose_name="Kursnomi ")
    photo = models.ImageField(upload_to="new/photos/", null=True, blank=True)
    def __str__(self):
        return f" {self.name}"
    class  Meta:
        verbose_name_plural = "Kurslar "
        verbose_name = "Kurs "

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=200, verbose_name="Dars nomi ")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name="Kurs nomi")
    video = models.FileField(upload_to="new/videos/", null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi'])])
    date = models.DateField(null=True, blank=True, verbose_name="Dars sanasi")
    summary = models.TextField(verbose_name="Dars Haqida")
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.lesson_name} {self.course} {self.date} {self.summary}"
    class  Meta:
        verbose_name_plural = "Darslar "
        verbose_name = "Dars "


class Comment(models.Model):
    text = models.TextField(verbose_name="Dars haqida firkingizni qoldiring ")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True )


    def __str__(self):
        return f"{self.user.username}"