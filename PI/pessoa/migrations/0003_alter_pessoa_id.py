# Generated by Django 4.1.13 on 2024-10-20 22:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_alter_pessoa_data_nascimento_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
