# Generated by Django 5.0 on 2024-01-22 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0014_pages_seo_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]