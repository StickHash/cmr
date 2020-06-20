# Generated by Django 3.0.6 on 2020-06-13 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20200608_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.IntegerField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(null=True, upload_to='recipes/steps/')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Recipe')),
            ],
        ),
    ]