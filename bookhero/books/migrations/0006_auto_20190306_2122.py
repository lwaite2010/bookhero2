# Generated by Django 2.1.7 on 2019-03-06 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20190306_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='open_library_url',
            field=models.CharField(default=None, max_length=255),
        ),
    ]