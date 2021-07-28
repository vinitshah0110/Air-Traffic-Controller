# Generated by Django 2.2.5 on 2019-09-22 09:13

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('distance', models.DecimalField(decimal_places=2, default=100.0, max_digits=100, validators=[django.core.validators.MinValueValidator(50)])),
                ('time_required', models.CharField(max_length=10)),
                ('fuel_required', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ending_atc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='path_ending_atc', to='atc.Atc')),
                ('starting_atc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='path_starting_atc', to='atc.Atc')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('starting_time', models.DateTimeField(default=datetime.datetime.now)),
                ('expected_end', models.DateTimeField(default=datetime.datetime.now)),
                ('ending_time', models.DateTimeField(default=datetime.datetime.now)),
                ('height', models.IntegerField(default=0)),
                ('distance', models.IntegerField(default=1000)),
                ('fuel', models.IntegerField(default=5000)),
                ('landing_type', models.BooleanField(default=False)),
                ('emergency_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('states', models.PositiveSmallIntegerField(choices=[(0, 'IDLE'), (1, 'TAKEOFF_DONE'), (2, 'IN_AIR'), (3, 'EMERGENCY'), (4, 'LANDING'), (5, 'LANDED')], default=0)),
                ('ending_atc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ending_atc', to='atc.Atc')),
                ('path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.Path')),
                ('starting_atc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starting_atc', to='atc.Atc')),
            ],
        ),
    ]
