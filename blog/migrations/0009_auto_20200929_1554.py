# Generated by Django 3.0.6 on 2020-09-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200929_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(upload_to='resume'),
        ),
    ]
