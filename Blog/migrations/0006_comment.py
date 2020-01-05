# Generated by Django 2.2.7 on 2019-12-05 15:22

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_blog_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=50)),
                ('lName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('pubdate', models.DateTimeField(default=datetime.datetime(2019, 12, 5, 15, 22, 48, 441778, tzinfo=utc))),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.Blog')),
            ],
        ),
    ]