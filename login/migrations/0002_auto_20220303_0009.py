# Generated by Django 3.2.7 on 2022-03-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='Email',
            field=models.EmailField(default='none@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='users',
            name='Password',
            field=models.CharField(default='jmd', max_length=100),
        ),
        migrations.AddField(
            model_name='users',
            name='PhoneNumber',
            field=models.IntegerField(default='9161967179'),
        ),
    ]