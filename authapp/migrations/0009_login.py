# Generated by Django 2.2 on 2019-11-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_delete_signin'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=10)),
                ('pwd', models.CharField(max_length=10)),
            ],
        ),
    ]
