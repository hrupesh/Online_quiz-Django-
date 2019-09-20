# Generated by Django 2.1.12 on 2019-09-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0014_auto_20190919_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='student_individual_test_details',
            name='tag',
        ),
        migrations.AddField(
            model_name='question',
            name='tag_name',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
