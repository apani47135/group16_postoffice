# Generated by Django 3.0.5 on 2020-04-03 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('sender_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('package_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('package_type', models.CharField(max_length=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('signature', models.BooleanField(default=False)),
                ('delivery_status', models.BooleanField(default=False)),
                ('order_date', models.DateField(verbose_name='Date Sent')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postoffice.Sender')),
            ],
        ),
    ]
