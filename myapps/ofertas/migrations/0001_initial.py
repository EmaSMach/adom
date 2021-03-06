# Generated by Django 3.1.1 on 2020-10-02 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myapps.ofertas.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_portada', models.ImageField(blank=True, default='img/ofertas/por_defecto/oferta-img.jpg', null=True, upload_to=myapps.ofertas.models.get_image_path)),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.TextField(blank=True, default='Sin descripción', null=True)),
                ('precio', models.IntegerField(blank=True, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('categorias', models.ManyToManyField(blank=True, related_name='ofertas', to='categorias.Categoria')),
                ('ofertante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ofertas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImagenOferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, default='img/ofertas/por_defecto/oferta-img.jpg', null=True, upload_to=myapps.ofertas.models.get_image_path)),
                ('fecha_subido', models.DateTimeField(auto_now_add=True)),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='ofertas.oferta')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Imagen de Oferta',
                'verbose_name_plural': 'Imágenes de Oferta',
            },
        ),
    ]
