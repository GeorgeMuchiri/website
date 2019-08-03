from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    #slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Sermon(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateField()
    recently_added = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    audi = models.FileField(default=None, null= True, blank=True)
    notes = models.FileField(default=None, null=True, blank=True)
    #slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.title

class Messages(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.name

class Announcements(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    by_who = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Announcements'

    def __str__(self):
        return self.title
