# Generated by Django 2.0.2 on 2020-06-26 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagefun', models.ImageField(upload_to='images/')),
                ('summury', models.CharField(max_length=200)),
            ],
        ),
    ]
