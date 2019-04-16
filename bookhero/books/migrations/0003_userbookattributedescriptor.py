# Generated by Django 2.1.7 on 2019-04-16 21:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attributes', '0002_attributedescriptor'),
        ('user_profiles', '0006_auto_20190411_0013'),
        ('books', '0002_book_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookAttributeDescriptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('descriptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attributes.AttributeDescriptor')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_profiles.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
