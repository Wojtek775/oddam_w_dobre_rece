# Generated by Django 3.2.4 on 2021-06-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=64)),
                ('type', models.IntegerField(choices=[(1, 'fundacja'), (2, 'organizacja pozarządowa'), (3, 'Zbiórka lokalna'), (4, 'domyślnie fundacja')])),
                ('categories', models.ManyToManyField(to='charity_app.Category')),
            ],
        ),
    ]
