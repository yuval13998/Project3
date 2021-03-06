# Generated by Django 2.0.3 on 2020-04-16 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timedate', models.CharField(max_length=30)),
                ('sum_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('islg', models.BooleanField()),
                ('sum_price', models.FloatField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lg', models.FloatField()),
                ('sm', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='orders', to='orders.Topping'),
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Price'),
        ),
        migrations.AddField(
            model_name='menu',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Type'),
        ),
    ]
