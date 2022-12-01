# Generated by Django 4.1.3 on 2022-11-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempstat',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='tempstat',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='tempstat',
            name='level',
        ),
        migrations.AddField(
            model_name='tempstat',
            name='annual_mean',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempstat',
            name='moving_mean',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempstat',
            name='year',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]