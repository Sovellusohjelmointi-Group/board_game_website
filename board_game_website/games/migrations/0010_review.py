# Generated by Django 4.1.3 on 2022-12-10 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0009_alter_games_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_review', models.TextField()),
                ('Games', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.games')),
            ],
        ),
    ]