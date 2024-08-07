# Generated by Django 5.0.6 on 2024-07-16 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.CharField(max_length=255)),
                ('original_title', models.CharField(max_length=1000)),
                ('overview', models.TextField()),
                ('popularity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('release_date', models.DateField()),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
