# Generated by Django 3.1.2 on 2020-11-18 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_title', models.CharField(max_length=70)),
                ('notice_text', models.CharField(max_length=400)),
                ('pub_start', models.DateTimeField()),
                ('pub_end', models.DateTimeField()),
            ],
        ),
    ]
