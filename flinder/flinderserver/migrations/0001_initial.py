# Generated by Django 2.2.26 on 2022-03-10 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestsAndPriorities',
            fields=[
                ('poster', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('pets', models.BooleanField()),
                ('food', models.BooleanField()),
                ('sports', models.BooleanField()),
                ('music', models.BooleanField()),
                ('partying', models.BooleanField()),
                ('drinking', models.BooleanField()),
                ('flatCleanliness', models.BooleanField()),
                ('strictQuietHours', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('poster', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mixedGender', models.BooleanField()),
                ('mixedYearOfStudy', models.BooleanField()),
                ('mixedAge', models.BooleanField()),
                ('maximumDistance', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=128)),
                ('lastName', models.CharField(max_length=128)),
                ('emailAddress', models.EmailField(max_length=128, unique=True)),
                ('dateOfBirth', models.DateField()),
                ('flatSearcher', models.BooleanField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('PNTS', 'Prefer not to say')], max_length=4)),
                ('yearOfStudy', models.CharField(choices=[('1', '1st Year'), ('2', '2nd Year'), ('3', '3rd Year'), ('4', '4th Year'), ('5', '5th Year'), ('PGT', 'Postgraduate')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Swipe',
            fields=[
                ('swipeID', models.AutoField(primary_key=True, serialize=False)),
                ('swipeRight', models.BooleanField()),
                ('swiped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swiped', to='flinderserver.UserProfile')),
                ('swiper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swiper', to='flinderserver.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('pictureID', models.AutoField(primary_key=True, serialize=False)),
                ('picture', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=256)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]