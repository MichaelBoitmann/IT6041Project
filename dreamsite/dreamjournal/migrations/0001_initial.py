# Generated by Django 3.2.3 on 2021-06-15 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('content', models.TextField(max_length=500)),
                ('type', models.CharField(blank=True, choices=[('Dream', 'Dream'), ('Nightmare', 'Nightmare')], max_length=10)),
                ('category', models.CharField(blank=True, choices=[('Reality', 'Reality'), ('Fantasy/Unreal', 'Fantasy/Unreal')], max_length=15)),
                ('colors_seen', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Orange', 'Orange'), ('Violet', 'Violet'), ('Brown', 'Brown'), ('Black', 'Black'), ('White', 'White')], max_length=53)),
                ('likes', models.IntegerField(default=0)),
                ('privacy', models.IntegerField(choices=[(0, 'Public'), (1, 'Private')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
