# Generated by Django 3.1 on 2020-09-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200903_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='courseDesc',
            field=models.CharField(blank=True, max_length=450),
        ),
        migrations.AddField(
            model_name='courses',
            name='courseRating',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='courses',
            name='courseTitle',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='courses',
            name='link1',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='courses',
            name='link2',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='courses',
            name='link3',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='courses',
            name='link4',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='courses',
            name='link5',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='courses',
            name='link6',
            field=models.CharField(default=0, max_length=250),
        ),
        migrations.AddField(
            model_name='courses',
            name='priceAfterDiscount',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='courses',
            name='priceBeforeDiscount',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
