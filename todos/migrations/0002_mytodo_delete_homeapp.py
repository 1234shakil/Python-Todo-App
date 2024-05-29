# Generated by Django 5.0.6 on 2024-05-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mytodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('complate', models.BooleanField(default=False)),
                ('createDate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Homeapp',
        ),
    ]
