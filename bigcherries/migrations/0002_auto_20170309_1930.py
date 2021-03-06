# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bigcherries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientConversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multiplicand', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IngredientRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigcherries.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigcherries.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='ingredientrecipe',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigcherries.MeasurementUnit'),
        ),
        migrations.AddField(
            model_name='ingredientconversion',
            name='dst_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bigcherries.MeasurementUnit'),
        ),
        migrations.AddField(
            model_name='ingredientconversion',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigcherries.Ingredient'),
        ),
        migrations.AddField(
            model_name='ingredientconversion',
            name='src_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bigcherries.MeasurementUnit'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='preferred_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigcherries.MeasurementUnit'),
        ),
    ]
