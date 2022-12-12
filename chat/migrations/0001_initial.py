from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=24)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('fav_num', models.IntegerField(default=0)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                #('img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]