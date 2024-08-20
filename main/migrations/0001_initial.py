# Generated by Django 4.2 on 2024-08-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrokerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('expected_transaction_amounts_per_month', models.DecimalField(decimal_places=2, max_digits=10)),
                ('region', models.CharField(max_length=255)),
                ('years_of_experience', models.PositiveIntegerField()),
            ],
        ),
    ]
