# Generated by Django 3.2.9 on 2021-11-29 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_complaint'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='complaint',
            new_name='complaint_table',
        ),
    ]