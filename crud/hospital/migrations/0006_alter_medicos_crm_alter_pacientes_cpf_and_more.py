# Generated by Django 5.1.1 on 2024-10-19 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_remove_medicos_horarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='crm',
            field=models.CharField(max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='idade',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_horario', models.DateTimeField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas_medico', to='hospital.medicos')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.pacientes')),
            ],
        ),
    ]