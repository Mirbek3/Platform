# Generated by Django 4.1.5 on 2023-01-14 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_course_course_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema_uroka', models.CharField(max_length=150)),
                ('opisaniye_temi', models.TextField()),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('junior', 'Начинающий'), ('middle', 'Продолжающий'), ('pro', 'Продвинутый')], max_length=15)),
                ('course', models.ManyToManyField(to='main_page.course')),
            ],
        ),
    ]
