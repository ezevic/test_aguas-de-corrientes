# Generated by Django 4.1.2 on 2022-10-26 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='palindromo',
            options={'ordering': ['update_at']},
        ),
    ]
