# Generated by Django 4.1.7 on 2023-05-04 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("visualizers_manager", "0014_alter_visualizerreport_report"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="visualizerreport",
            unique_together=set(),
        ),
    ]