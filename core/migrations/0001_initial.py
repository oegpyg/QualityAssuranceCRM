# Generated by Django 4.2.1 on 2023-05-31 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=50)),
                ('target_flow', models.CharField(max_length=50)),
            ],
        ),
    ]