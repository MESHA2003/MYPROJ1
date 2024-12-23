# Generated by Django 5.1.4 on 2024-12-21 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyDiary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diaryentrytag',
            name='diary_entry',
        ),
        migrations.RemoveField(
            model_name='diaryentrytag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='usersetting',
            name='user',
        ),
        migrations.DeleteModel(
            name='DiaryEntry',
        ),
        migrations.DeleteModel(
            name='DiaryEntryTag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='UserSetting',
        ),
    ]
