# Generated by Django 2.1.2 on 2020-07-17 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0002_registrohoraextra_funcionanrio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrohoraextra',
            old_name='funcionanrio',
            new_name='funcionario',
        ),
    ]
