# Generated by Django 5.0.6 on 2024-07-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='new_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
