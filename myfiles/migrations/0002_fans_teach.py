# Generated by Django 4.0.4 on 2022-09-14 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('fam', models.CharField(max_length=30)),
                ('yosh', models.IntegerField()),
                ('sana', models.DateField()),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.fan')),
            ],
        ),
    ]
