# Generated by Django 4.2.8 on 2024-04-20 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('account_number', models.CharField(editable=False, max_length=20, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('service_issue', 'Service Issue'), ('billing_inquiry', 'Billing Inquiry'), ('other', 'Other')], max_length=20)),
                ('details', models.TextField()),
                ('files', models.FileField(upload_to='service_request_files/')),
                ('status', models.CharField(max_length=20)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('date_resolved', models.DateTimeField(null=True)),
                ('track_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumer_services.customer')),
            ],
        ),
    ]