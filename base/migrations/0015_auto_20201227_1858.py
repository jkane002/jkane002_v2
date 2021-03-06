# Generated by Django 3.1.4 on 2020-12-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20201227_0321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpost',
            name='image',
        ),
        migrations.AddField(
            model_name='projectpost',
            name='challenge',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectpost',
            name='enjoyed',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectpost',
            name='leadership',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectpost',
            name='mistake',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectpost',
            name='possible_revisions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
