# Generated by Django 3.0.5 on 2021-02-28 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='**No-Name**', max_length=255)),
                ('pizza_shape', models.CharField(choices=[('REGULAR', 'REGULAR'), ('SQUARE', 'SQUARE')], default='REGULAR', max_length=200)),
                ('pizza_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Size')),
                ('pizza_topping', models.ManyToManyField(to='pizza.Topping')),
            ],
        ),
    ]