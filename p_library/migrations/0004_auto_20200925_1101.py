# Generated by Django 2.2.6 on 2020-09-25 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20200925_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publishing_house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.PublishingHouse', verbose_name='Издательство'),
        ),
    ]
