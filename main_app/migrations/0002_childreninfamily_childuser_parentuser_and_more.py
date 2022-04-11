# Generated by Django 4.0.3 on 2022-04-10 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildrenInFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ChildUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=250, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('unique_family_name', models.CharField(max_length=100)),
                ('is_child', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('identifier', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParentUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=250)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Parent', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('unique_family_name', models.CharField(max_length=100)),
                ('is_parent', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('identifier', models.CharField(max_length=40, unique=True)),
                ('family_children', models.ManyToManyField(through='main_app.ChildrenInFamily', to='main_app.childuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='FamilyGroup',
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('Incomplete', 'incomplete'), ('Not yet started', 'not yet started'), ('Completed', 'complete')], max_length=20),
        ),
        migrations.AddField(
            model_name='childreninfamily',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_child_first_name', to='main_app.childuser'),
        ),
        migrations.AddField(
            model_name='childreninfamily',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_parent', to='main_app.parentuser'),
        ),
        migrations.AlterUniqueTogether(
            name='childreninfamily',
            unique_together={('parent', 'child')},
        ),
    ]
