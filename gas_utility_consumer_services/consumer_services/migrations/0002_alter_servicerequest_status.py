# Generated by Django 4.2.8 on 2024-04-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer_services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(default='submitted', max_length=20),
        ),
    ]
