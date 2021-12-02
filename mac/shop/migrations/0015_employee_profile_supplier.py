# Generated by Django 3.2.9 on 2021-11-30 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0014_cancel_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('Designation', models.CharField(max_length=50)),
                ('Adhaar_id', models.IntegerField()),
                ('joining_date', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('joining_date', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='main.jpg', upload_to='profile_imgs')),
                ('address', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]