# Generated by Django 4.1.1 on 2022-09-24 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('cod_administrador', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('Contraseña', models.CharField(max_length=255)),
            ],
        ),
    ]