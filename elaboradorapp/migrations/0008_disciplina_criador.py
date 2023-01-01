# Generated by Django 4.1.3 on 2023-01-01 00:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('elaboradorapp', '0007_rename_autor_question_vinculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='criador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
