# Generated by Django 4.0.4 on 2022-05-31 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogApp', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='media'),
        ),
    ]
