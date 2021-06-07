# Generated by Django 3.2 on 2021-06-07 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intentos_por_IP',
            fields=[
                ('ip', models.GenericIPAddressField(primary_key=True, serialize=False)),
                ('contador', models.IntegerField(default=0)),
                ('ultima_peticion', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=1024)),
                ('Email', models.EmailField(max_length=254)),
                ('Telefono', models.CharField(max_length=10)),
                ('token_telegram', models.CharField(default='', max_length=128)),
                ('chat_id', models.CharField(default='', max_length=32)),
                ('codigoTelegram', models.CharField(default='', max_length=5)),
                ('tiempo_de_vida', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Confianza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarioRegistrado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroUsuario.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Cuenta', models.CharField(max_length=100)),
                ('password_Asociado', models.CharField(max_length=1024)),
                ('url_Asociado', models.URLField(max_length=1024)),
                ('detalles_Asociado', models.CharField(max_length=1024)),
                ('iv', models.CharField(max_length=16)),
                ('usuario_Asociado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registroUsuario.usuario')),
            ],
        ),
    ]
