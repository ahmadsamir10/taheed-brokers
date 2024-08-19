# Generated by Django 4.0 on 2024-06-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_content', models.TextField(blank=True, null=True)),
                ('display_banner', models.BooleanField(default=True)),
                ('stop_renting', models.BooleanField(default=False)),
                ('company_bank_details', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
