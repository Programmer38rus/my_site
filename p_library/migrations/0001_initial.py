# Generated by Django 2.2.6 on 2020-09-24 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('birth_year', models.SmallIntegerField()),
                ('country', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='Empty', max_length=100)),
                ('count_book', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('year_release', models.SmallIntegerField()),
                ('price', models.FloatField()),
                ('copy_count', models.SmallIntegerField(default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Author', verbose_name='Вербос_нэйм')),
                ('publishing_house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='p_library.PublishingHouse', verbose_name='Издательство')),
            ],
        ),
    ]
