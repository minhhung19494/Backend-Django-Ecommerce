# Generated by Django 2.2.4 on 2020-02-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200216_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemvariation',
            name='value',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='variation',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
