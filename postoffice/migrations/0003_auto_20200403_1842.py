# Generated by Django 3.0.5 on 2020-04-03 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postoffice', '0002_auto_20200403_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='branches',
            fields=[
                ('branch_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('zipcode', models.IntegerField()),
                ('address', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='reciever',
            fields=[
                ('reciever_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='sender',
            name='pub_date',
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=4)),
                ('address', models.CharField(max_length=60)),
                ('works_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postoffice.branches')),
            ],
        ),
        migrations.AddField(
            model_name='packages',
            name='current_location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='postoffice.branches'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packages',
            name='reciever',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='postoffice.reciever'),
            preserve_default=False,
        ),
    ]
