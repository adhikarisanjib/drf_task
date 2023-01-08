# Generated by Django 4.1.5 on 2023-01-07 08:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('age', models.PositiveSmallIntegerField(max_length=2, verbose_name='Age')),
                ('address', models.CharField(help_text='In format city - ward no., district, country.', max_length=255, verbose_name='Address')),
                ('grade', models.PositiveSmallIntegerField(help_text='Must be between 1 to 12.', max_length=2, verbose_name='Grade')),
                ('major', models.CharField(max_length=255, verbose_name='Major')),
            ],
        ),
    ]
