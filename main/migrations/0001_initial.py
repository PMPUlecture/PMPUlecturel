# Generated by Django 3.1.2 on 2020-11-23 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('apmath_url', models.URLField(max_length=256, null=True)),
                ('vk_discuss_url', models.URLField(max_length=256, null=True)),
                ('photo_url', models.URLField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('img_url', models.URLField(max_length=256)),
                ('degree', models.CharField(choices=[('bachelor', 'Бакалавриат'), ('master', 'Магистратура')], max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('term', models.IntegerField(null=True)),
                ('programme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.programme')),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
                ('type', models.CharField(choices=[('abstract', 'конспект'), ('questions', 'вопросы'), ('test', 'контрльная'), ('other', 'разное')], max_length=16)),
                ('link', models.URLField(max_length=256, null=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.lecturer')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.subject')),
            ],
        ),
        migrations.AddField(
            model_name='lecturer',
            name='subject',
            field=models.ManyToManyField(null=True, to='main.Subject'),
        ),
    ]
