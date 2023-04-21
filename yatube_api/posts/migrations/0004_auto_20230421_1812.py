# Generated by Django 3.2.16 on 2023-04-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230421_1809'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='user_following',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='user',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='user_following'),
        ),
    ]
