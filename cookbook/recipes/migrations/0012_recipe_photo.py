# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-30 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_remove_recipe_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(default='media/none', upload_to='media/'),
        ),
    ]
