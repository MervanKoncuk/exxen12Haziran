# Generated by Django 3.2.12 on 2022-07-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220719_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tur',
            field=models.ManyToManyField(to='movies.Tur', verbose_name='Film Türü'),
        ),
    ]