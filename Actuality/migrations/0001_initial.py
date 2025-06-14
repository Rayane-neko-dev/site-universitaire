# Generated by Django 5.1.6 on 2025-06-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actualite_id', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/actuality')),
                ('titre', models.CharField(max_length=100)),
                ('contenu', models.CharField(max_length=1000)),
                ('date', models.DateField()),
            ],
        ),
    ]
