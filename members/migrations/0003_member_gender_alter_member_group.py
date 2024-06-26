# Generated by Django 5.0.6 on 2024-05-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literals', '0001_initial'),
        ('members', '0002_alter_member_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='group',
            field=models.ManyToManyField(blank=True, to='literals.group'),
        ),
    ]
