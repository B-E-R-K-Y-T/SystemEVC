# Generated by Django 5.1.3 on 2024-11-19 19:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ServerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkPriority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255)),
                ('internal_ip', models.GenericIPAddressField()),
                ('external_ip', models.GenericIPAddressField()),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cpu_info', models.TextField()),
                ('ram_size', models.CharField(max_length=50)),
                ('disk_size', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notification.location')),
                ('os', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notification.operatingsystem')),
                ('server_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notification.servertype')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('internal_ip', models.GenericIPAddressField()),
                ('port', models.IntegerField()),
                ('url', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.CharField(max_length=255)),
                ('protocol', models.CharField(max_length=50)),
                ('dependencies', models.TextField(blank=True)),
                ('health_check_url', models.URLField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('last_maintenance_date', models.DateField(blank=True, null=True)),
                ('version', models.CharField(blank=True, max_length=50)),
                ('availability_zone', models.CharField(blank=True, max_length=255)),
                ('server', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notification.server')),
                ('service_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notification.servicetype')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notification.workstatus')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDependency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependency_type', models.CharField(max_length=255)),
                ('dependency_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependent_services', to='notification.service')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_dependencies', to='notification.service')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('work_plan', models.TextField()),
                ('rollback_plan', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('duration_estimation', models.FloatField()),
                ('dependencies', models.TextField(blank=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('cancelled_at', models.DateTimeField(blank=True, null=True)),
                ('last_updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='works_last_updated', to=settings.AUTH_USER_MODEL)),
                ('user_ids_works', models.ManyToManyField(related_name='works_conducted', to=settings.AUTH_USER_MODEL)),
                ('user_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='works_managed', to=settings.AUTH_USER_MODEL)),
                ('priority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notification.workpriority')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notification.workstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('time_long_end', models.DateTimeField()),
                ('is_read', models.BooleanField(default=False)),
                ('external_reference', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notification.work')),
            ],
        ),
        migrations.CreateModel(
            name='WorkLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True)),
                ('changed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.work')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notification.workstatus')),
            ],
        ),
    ]