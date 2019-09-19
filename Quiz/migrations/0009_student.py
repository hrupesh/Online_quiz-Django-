# Generated by Django 2.1.12 on 2019-09-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0008_auto_20190917_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_Registration_Number', models.CharField(max_length=15, unique=True)),
                ('First_Name', models.CharField(max_length=15, unique=True)),
                ('Last_Name', models.CharField(max_length=250)),
                ('Graduation_Year', models.IntegerField()),
                ('Branch', models.CharField(max_length=250)),
                ('Course', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=100)),
                ('Phone_Number', models.IntegerField()),
                ('Score', models.IntegerField()),
                ('Login_Count', models.IntegerField()),
                ('Password', models.CharField(max_length=250)),
            ],
        ),
    ]
