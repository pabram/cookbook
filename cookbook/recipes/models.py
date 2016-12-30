from django.db import models
from django.template.defaultfilters import slugify
from django.contrib import admin
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=300, default="")
    content = models.TextField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
    photo = models.FileField(null=True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
