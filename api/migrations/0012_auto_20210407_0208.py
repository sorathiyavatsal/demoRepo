# Generated by Django 3.1.7 on 2021-04-06 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('chat_date', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('chat_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_from_user', to='api.user')),
                ('chat_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_to_user', to='api.user')),
                ('trip_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_trip', to='api.trip')),
            ],
            options={
                'db_table': 'chats',
            },
        ),
        migrations.AddIndex(
            model_name='chatmodel',
            index=models.Index(fields=['id', 'chat_to', 'chat_from', 'trip_id', 'message', 'chat_date'], name='chats_id_a28ef2_idx'),
        ),
    ]
