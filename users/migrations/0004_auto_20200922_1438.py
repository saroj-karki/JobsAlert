# Generated by Django 3.0.6 on 2020-09-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_account_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]