# Generated by Django 4.1.3 on 2022-12-01 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_student_delete_aames'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='games',
            name='authors',
        ),
        migrations.AddField(
            model_name='games',
            name='semester',
            field=models.CharField(choices=[('N', 'NO'), ('Y', 'YES')], default='N', max_length=20),
        ),
    ]
