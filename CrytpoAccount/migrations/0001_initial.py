# Generated by Django 3.2.8 on 2023-05-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/images')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=25)),
                ('zipcode', models.CharField(max_length=6)),
                ('adharCard', models.ImageField(blank=True, null=True, upload_to='upload/images')),
                ('PanCard', models.ImageField(blank=True, null=True, upload_to='upload/images')),
            ],
        ),
    ]