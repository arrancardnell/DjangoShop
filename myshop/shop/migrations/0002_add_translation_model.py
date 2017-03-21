# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('language_code', models.CharField(verbose_name='Language', max_length=15, db_index=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'verbose_name': 'category Translation',
                'db_tablespace': '',
                'default_permissions': (),
                'managed': True,
                'db_table': 'shop_category_translation',
            },
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('language_code', models.CharField(verbose_name='Language', max_length=15, db_index=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'product Translation',
                'db_tablespace': '',
                'default_permissions': (),
                'managed': True,
                'db_table': 'shop_product_translation',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([]),
        ),
        migrations.AddField(
            model_name='producttranslation',
            name='master',
            field=models.ForeignKey(related_name='translations', to='shop.Product', null=True, editable=False),
        ),
        migrations.AddField(
            model_name='categorytranslation',
            name='master',
            field=models.ForeignKey(related_name='translations', to='shop.Category', null=True, editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='producttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
