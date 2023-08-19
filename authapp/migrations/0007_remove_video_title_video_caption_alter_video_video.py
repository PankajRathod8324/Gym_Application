# Generated by Django 4.1.7 on 2023-04-10 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
        migrations.AddField(
            model_name='video',
            name='caption',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='upload_video/'),
        ),
    ]
