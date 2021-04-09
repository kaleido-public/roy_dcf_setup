# Generated by Django 3.1.4 on 2021-04-09 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='belong_group', to='persons.group'),
        ),
    ]
