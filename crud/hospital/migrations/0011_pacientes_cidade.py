# Generated by Django 5.0.7 on 2024-10-21 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_rename_endereco_pacientes_logradouro_pacientes_cep_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='cidade',
            field=models.CharField(default='', max_length=20),
        ),
    ]