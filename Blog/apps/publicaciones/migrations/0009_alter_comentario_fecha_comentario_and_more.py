# Generated by Django 5.1.1 on 2024-10-10 22:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0008_alter_comentario_fecha_comentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 10, 22, 30, 6, 376906, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_creacion_public',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 10, 22, 30, 6, 375905, tzinfo=datetime.timezone.utc)),
        ),
    ]
