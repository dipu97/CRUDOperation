# Generated by Django 3.1.7 on 2021-03-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=35)),
                ('education', models.CharField(max_length=250)),
            ],
        ),
    ]
