# Generated by Django 3.0.8 on 2020-09-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=300)),
                ('category', models.CharField(blank=True, max_length=64)),
                ('start_bid', models.FloatField()),
                ('image', models.URLField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]