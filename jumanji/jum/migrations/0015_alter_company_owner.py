# Generated by Django 4.0.2 on 2022-03-18 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jum', '0014_alter_company_logo_alter_specialty_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(blank=True,
                                       null=True,
                                       on_delete=django.db.models.deletion.CASCADE,
                                       to=settings.AUTH_USER_MODEL),
        ),
    ]
