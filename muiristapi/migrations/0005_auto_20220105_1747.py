# Generated by Django 3.2.11 on 2022-01-05 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('muiristapi', '0004_snippet_lists'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ParkData',
        ),
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='snippetlist',
            name='snippets',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippet_lists', to='muiristapi.snippet'),
        ),
    ]
