# Generated by Django 2.2.16 on 2020-10-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200929_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile-pic-default.png', upload_to='profile_pics'),
        ),
    ]
