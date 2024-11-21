# Generated by Django 5.1.3 on 2024-11-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('size', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('age_limited', models.BooleanField(default=False)),
                ('buyers', models.ManyToManyField(related_name='games', to='task1.buyer')),
            ],
        ),
    ]