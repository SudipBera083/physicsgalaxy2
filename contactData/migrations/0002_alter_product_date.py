# Generated by Django 3.2.6 on 2021-09-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.CharField(default='none', max_length=50),
        ),
    ]