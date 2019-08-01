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
    audi = models.FileField(upload_to='audio/', default=None, null= True, blank=True)
    notes = models.FileField(upload_to='notes/', default=None, null=True, blank=True)
    #slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.title
