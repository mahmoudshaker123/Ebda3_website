# Generated by Django 5.1.4 on 2025-02-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebda3', '0002_about_home_offer_alter_backgroundimage_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(default='https://www.facebook.com/ebda3design')),
                ('instgram', models.URLField(default='https://www.instagram.com/ebda3design')),
                ('location', models.CharField(default='شارع الغشام, Zagazig, Egypt', max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('email', models.EmailField(default='ebda3design2@gmail.com', max_length=254)),
                ('whatsapp_number', models.CharField(default='https://wa.me/201067343755', max_length=200)),
                ('location_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='office',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='about',
            name='projects',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='about',
            name='users',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='about',
            name='workers',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.DeleteModel(
            name='NumberStatistic',
        ),
    ]
