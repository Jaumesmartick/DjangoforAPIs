# Generated by Django 3.0.5 on 2020-04-15 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=15)),
            ],
        ),
    ]
