# Generated by Django 3.0.7 on 2020-07-09 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_item_stock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-stock']},
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
