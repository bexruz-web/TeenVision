# Generated by Django 5.2 on 2025-05-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('full_info', models.TextField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('link', models.URLField()),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('format', models.CharField(blank=True, choices=[('online', 'Online'), ('offline', 'Oflayn'), ('hybrid', 'Gibrid')], max_length=50, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='program_photos/')),
                ('type', models.CharField(choices=[('program', 'Dastur'), ('tutorial', 'Tutorial')], max_length=50)),
                ('funding', models.CharField(blank=True, choices=[('full', "To'liq moliyalashtiriladi"), ('partial', 'Qisman moliyalashtiriladi'), ('self', "O'zi to'laydi"), ('sponsorship', 'Sponsorlik orqali')], max_length=100, null=True)),
                ('start_age', models.PositiveIntegerField(blank=True, null=True)),
                ('end_age', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Erkaklar uchun'), ('female', 'Ayollar uchun'), ('any', 'Hamma uchun')], max_length=10, null=True)),
                ('status', models.CharField(choices=[('on', 'Faol'), ('off', 'Nofaol')], default='on', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('major', models.ManyToManyField(blank=True, to='core.major')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
