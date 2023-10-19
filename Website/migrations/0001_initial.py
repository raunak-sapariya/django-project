# Generated by Django 4.2.6 on 2023-10-15 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('unitId', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('youtubeSearchQuery', models.CharField(max_length=255)),
                ('videoId', models.CharField(blank=True, max_length=255, null=True)),
                ('summary', models.CharField(blank=True, max_length=3000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('courseId', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='Website.course')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('chapterId', models.CharField(max_length=255)),
                ('question', models.CharField(max_length=3000)),
                ('answer', models.CharField(max_length=3000)),
                ('options', models.CharField(max_length=3000)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='Website.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='Website.unit'),
        ),
    ]
