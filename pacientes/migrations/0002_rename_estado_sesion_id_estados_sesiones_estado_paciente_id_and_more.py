# Generated by Django 4.1.5 on 2023-05-03 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estados_sesiones',
            old_name='estado_sesion_id',
            new_name='estado_paciente_id',
        ),
        migrations.RemoveField(
            model_name='estados_sesiones',
            name='descripcion_estado_sesion',
        ),
        migrations.AddField(
            model_name='estados_sesiones',
            name='estado_paciente_descripcion',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
