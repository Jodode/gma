# Generated by Django 4.1.7 on 2023-06-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futbik', '0012_alter_hit_angle_alter_hit_footed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hit',
            name='footed',
        ),
        migrations.AddField(
            model_name='players',
            name='footed',
            field=models.CharField(default='right', max_length=10),
        ),
    ]
