# Generated by Django 3.2.6 on 2021-08-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_auto_20210803_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='identifier',
            new_name='registration_number',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('MANAGER', 'Manager'), ('LEADER', 'Leader'), ('USER', 'Member')], default='USER', max_length=20),
        ),
    ]
