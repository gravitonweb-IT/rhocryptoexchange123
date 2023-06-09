# Generated by Django 3.2.8 on 2023-05-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrytpoAccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CryptPrice', models.CharField(max_length=150)),
                ('IndianPrice', models.CharField(max_length=150)),
                ('PayementScreenShot', models.ImageField(blank=True, null=True, upload_to='upload/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='signupmodel',
            name='zipcode',
        ),
    ]
