# Generated by Django 3.1.4 on 2020-12-22 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_projectpostimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpostimage',
            name='post',
            field=models.ForeignKey(default='images/placeholder.png', null=True, on_delete=django.db.models.deletion.CASCADE, to='base.projectpost'),
        ),
    ]
