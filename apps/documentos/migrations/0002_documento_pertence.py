# Generated by Django 2.1.2 on 2020-07-17 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='pertence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionarios.Funcionario'),
        ),
    ]