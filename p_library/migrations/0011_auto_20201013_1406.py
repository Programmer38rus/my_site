# Generated by Django 2.2.6 on 2020-10-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0010_auto_20201013_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.TextField(max_length=100),
        ),
    ]
