# Generated by Django 2.2.6 on 2020-10-13 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0011_auto_20201013_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
    ]
