# Generated by Django 3.0.5 on 2020-05-02 09:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning_logs', '0005_auto_20200502_0849'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='entry',
            name='unique_user',
        ),
        migrations.RemoveConstraint(
            model_name='topic',
            name='unique_owner',
        ),
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='entry',
            unique_together={('topic', 'text')},
        ),
        migrations.AlterUniqueTogether(
            name='topic',
            unique_together={('text', 'owner')},
        ),
    ]