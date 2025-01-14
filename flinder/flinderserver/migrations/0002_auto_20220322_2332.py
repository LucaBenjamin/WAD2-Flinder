# Generated by Django 2.2.26 on 2022-03-22 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flinderserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interestsandpriorities',
            options={'verbose_name_plural': 'Interests and Priorities'},
        ),
        migrations.AlterModelOptions(
            name='pictures',
            options={'verbose_name_plural': 'Pictures'},
        ),
        migrations.AlterModelOptions(
            name='preferences',
            options={'verbose_name_plural': 'Preferences'},
        ),
        migrations.AlterModelOptions(
            name='swipe',
            options={'verbose_name_plural': 'Swipe Actions'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'User Profiles'},
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='interestsandpriorities',
            name='drinking',
        ),
        migrations.RemoveField(
            model_name='interestsandpriorities',
            name='flatCleanliness',
        ),
        migrations.RemoveField(
            model_name='interestsandpriorities',
            name='food',
        ),
        migrations.RemoveField(
            model_name='interestsandpriorities',
            name='music',
        ),
        migrations.RemoveField(
            model_name='interestsandpriorities',
            name='partying',
        ),
        migrations.RemoveField(
            model_name='interestsandpriorities',
            name='pets',
        ),
        migrations.RemoveField(
            model_name='interestsandpriorities',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='interestsandpriorities',
            name='sports',
        ),
        migrations.RemoveField(
            model_name='interestsandpriorities',
            name='strictQuietHours',
        ),
        migrations.RemoveField(
            model_name='preferences',
            name='maximumDistance',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='emailAddress',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='lastName',
        ),
        migrations.AddField(
            model_name='interestsandpriorities',
            name='choice',
            field=models.CharField(default='error', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interestsandpriorities',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='addressLine1',
            field=models.CharField(default='nowhere', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='addressLine2',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='flatBedrooms',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='freeBedrooms',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='interests',
            field=models.ManyToManyField(to='flinderserver.InterestsAndPriorities'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mixedYearOfBirth',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='postCode',
            field=models.CharField(default=True, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='university',
            field=models.CharField(default=True, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='preferences',
            name='mixedAge',
            field=models.BooleanField(choices=[(True, 'Mixed'), (False, 'Same')]),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='mixedGender',
            field=models.BooleanField(choices=[(True, 'Mixed'), (False, 'Same')]),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='mixedYearOfStudy',
            field=models.BooleanField(choices=[(True, 'Mixed'), (False, 'Same')]),
        ),
        migrations.AlterField(
            model_name='swipe',
            name='swiped',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swiped', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='swipe',
            name='swiper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swiper', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('MIX', 'Mixed'), ('PNTS', 'Prefer not to say')], max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='yearOfStudy',
            field=models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year'), ('5', '5th Year'), ('PGT', 'Postgraduate'), ('MIX', 'Mixed')], max_length=2),
        ),
    ]
