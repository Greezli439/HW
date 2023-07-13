# Generated by Django 4.2.3 on 2023-07-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0009_quote_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='tags',
        ),
        migrations.AddField(
            model_name='quote',
            name='tags',
            field=models.TextField(default=None, null=True),
        ),
    ]
