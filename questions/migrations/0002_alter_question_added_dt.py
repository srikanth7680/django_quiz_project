# Generated by Django 4.2.7 on 2023-11-21 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='added_dt',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
