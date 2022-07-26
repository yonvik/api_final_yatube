# Generated by Django 4.0.6 on 2022-07-26 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220725_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='discription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.group'),
        ),
    ]
