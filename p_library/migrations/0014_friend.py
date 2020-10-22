# Generated by Django 2.2.6 on 2020-10-15 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0013_auto_20201013_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=99)),
                ('books', models.ManyToManyField(to='p_library.Book', verbose_name='Взяли в долг')),
            ],
        ),
    ]
