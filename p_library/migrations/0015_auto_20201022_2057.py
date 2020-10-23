# Generated by Django 2.2.6 on 2020-10-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0014_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='face',
            field=models.ImageField(blank=True, upload_to='face_author/%H/%s'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='full_name',
            field=models.CharField(max_length=99, verbose_name='Имя'),
        ),
    ]