# Generated by Django 4.2.2 on 2023-07-29 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_category_stored'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='stored',
        ),
    ]