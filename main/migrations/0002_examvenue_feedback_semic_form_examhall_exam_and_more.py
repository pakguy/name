# Generated by Django 5.0.3 on 2024-06-03 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamVenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=255, null=True)),
                ('course_code', models.CharField(max_length=15, null=True)),
                ('specific_feedback', models.CharField(max_length=455, null=True)),
                ('suggestion_for_improvement', models.CharField(max_length=455, null=True)),
                ('feedback_attachment', models.FileField(upload_to='feedback/attachments/')),
            ],
        ),
        migrations.CreateModel(
            name='Semic_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255, null=True)),
                ('matric_no', models.CharField(max_length=20, null=True)),
                ('course_title', models.CharField(max_length=255, null=True)),
                ('course_code', models.CharField(max_length=7, null=True)),
                ('student_comment', models.TextField(blank=True, null=True)),
                ('invigilator_comment', models.TextField(blank=True, null=True)),
                ('semic_attachment', models.FileField(upload_to='semic/attachments')),
            ],
        ),
        migrations.CreateModel(
            name='ExamHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('no_of_seats', models.IntegerField()),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.examvenue')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Paper Exam', 'Paper Exam'), ('CBT', 'CBT')], default='paper', max_length=20)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('course', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.examvenue')),
            ],
        ),
        migrations.CreateModel(
            name='invigilator_allocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invigilator', to='main.examhall')),
                ('invigilator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invigilator_allocations', to='main.invigilator')),
            ],
        ),
        migrations.CreateModel(
            name='student_allocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='main.examhall')),
                ('student_allocated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_allocations', to='main.student')),
            ],
        ),
    ]
