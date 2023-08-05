# Generated by Django 4.2.2 on 2023-08-05 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50)),
                ('academic_level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(blank=True)),
                ('genre', models.CharField(max_length=50)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolms.group')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
                ('first_tcp_mark', models.IntegerField(blank=True)),
                ('second_tcp_mark', models.IntegerField(blank=True)),
                ('final_test_mark', models.IntegerField(blank=True)),
                ('extra_test_mark', models.IntegerField(blank=True)),
                ('mundial_test_mark', models.IntegerField(blank=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolms.student')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolms.professor'),
        ),
    ]