# Generated by Django 4.1.7 on 2023-05-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbik', '0002_remove_championships_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineup',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
