# Generated by Django 4.0.3 on 2022-04-09 18:39

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.jpg', upload_to=blog.models.upload_to, verbose_name='Image'),
        ),
    ]
