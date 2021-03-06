# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-31 16:32
from __future__ import unicode_literals

import bitfield.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import edw.models.fields
import edw.models.term
import edw.signals.mptt
import email_auth.models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('email_auth', '0002_auto_20160327_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalEntityCharacteristicOrMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
                ('view_class', models.CharField(blank=True, help_text='Space delimited class attribute, specifies one or more classnames for an entity.', max_length=255, null=True, verbose_name='View Class')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Additional Entity Characteristic or Mark',
                'verbose_name_plural': 'Additional Entity Characteristics or Marks',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('active', models.BooleanField(default=True, help_text='Is this object publicly visible.', verbose_name='Active')),
                ('name', models.CharField(max_length=255, verbose_name='Book Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('order', models.PositiveIntegerField(db_index=True, default=1, verbose_name='Sort by')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('recognized', models.PositiveSmallIntegerField(choices=[(0, 'Unrecognized'), (1, 'Guest'), (2, 'Registered')], default=0, help_text='Designates the state the customer is recognized as.', verbose_name='Recognized as')),
                ('salutation', models.CharField(choices=[('mrs', 'Mrs.'), ('mr', 'Mr.'), ('na', '(n/a)')], max_length=5, verbose_name='Salutation')),
                ('last_access', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last accessed')),
                ('extra', jsonfield.fields.JSONField(default={}, editable=False, verbose_name='Extra information about this customer')),
                ('number', models.PositiveIntegerField(default=None, null=True, unique=True, verbose_name='Customer Number')),
            ],
        ),
        migrations.CreateModel(
            name='DataMart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(help_text='Used for URLs, auto-generated from name if blank', verbose_name='Slug')),
                ('path', models.CharField(db_index=True, editable=False, max_length=255, unique=True, verbose_name='Path')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('view_class', models.CharField(blank=True, help_text='Space delimited class attribute, specifies one or more classnames for an data mart.', max_length=255, null=True, verbose_name='View Class')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('active', models.BooleanField(db_index=True, default=True, help_text='Is this data mart active.', verbose_name='Active')),
                ('system_flags', bitfield.models.BitField([('delete_restriction', 'Delete restriction'), ('change_parent_restriction', 'Change parent restriction'), ('change_slug_restriction', 'Change slug restriction'), ('has_child_restriction', 'Has child restriction')], default=None, null=True, verbose_name='system flags')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', edw.models.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='sample.DataMart', verbose_name='Parent')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_sample.datamart_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Data mart',
                'verbose_name_plural': 'Data marts',
            },
            bases=(edw.signals.mptt.MPTTModelSignalSenderMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(help_text='Used for URLs, auto-generated from name if blank', verbose_name='Slug')),
                ('path', models.CharField(db_index=True, editable=False, max_length=255, unique=True, verbose_name='Path')),
                ('semantic_rule', models.PositiveSmallIntegerField(choices=[(10, 'OR'), (20, 'XOR'), (30, 'AND')], default=10, verbose_name='Semantic Rule')),
                ('attributes', bitfield.models.BitField([('is_characteristic', 'Is characteristic'), ('is_mark', 'Is mark'), ('is_relation', 'Is relation')], default=None, help_text='Specifying attributes of term.', null=True, verbose_name='attributes')),
                ('specification_mode', models.PositiveSmallIntegerField(choices=[(10, 'Standard'), (20, 'Expanded'), (30, 'Reduced')], default=10, verbose_name='Specification Mode')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('view_class', models.CharField(blank=True, help_text='Space delimited class attribute, specifies one or more classnames for an entity.', max_length=255, null=True, verbose_name='View Class')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('active', models.BooleanField(db_index=True, default=True, help_text='Is this term active.', verbose_name='Active')),
                ('system_flags', bitfield.models.BitField([('delete_restriction', 'Delete restriction'), ('change_parent_restriction', 'Change parent restriction'), ('change_slug_restriction', 'Change slug restriction'), ('change_semantic_rule_restriction', 'Change semantic rule restriction'), ('has_child_restriction', 'Has child restriction'), ('external_tagging_restriction', 'External tagging restriction')], default=None, null=True, verbose_name='system flags')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', edw.models.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='sample.Term', verbose_name='Parent')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Term',
                'verbose_name_plural': 'Topic model',
            },
            bases=(edw.models.term.AndRuleFilterMixin, edw.models.term.OrRuleFilterMixin, edw.signals.mptt.MPTTModelSignalSenderMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CustomerProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Customer',
                'proxy': True,
                'verbose_name_plural': 'Customers',
            },
            bases=('email_auth.user',),
            managers=[
                ('objects', email_auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdultBook',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sample.Book')),
                ('genre', models.PositiveSmallIntegerField(choices=[(1, 'Fantastic'), (2, 'Drama'), (3, 'Mistics')], verbose_name='Genre')),
            ],
            options={
                'verbose_name': 'Adult book',
                'verbose_name_plural': 'Adult books',
            },
            bases=('sample.book',),
        ),
        migrations.CreateModel(
            name='ChildBook',
            fields=[
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sample.Book')),
                ('age', models.PositiveSmallIntegerField(choices=[(1, '0-6 month'), (2, '6-12 month'), (3, '1+ year')], verbose_name='Age')),
            ],
            options={
                'verbose_name': 'Child book',
                'verbose_name_plural': 'Child books',
            },
            bases=('sample.book',),
        ),
        migrations.AddField(
            model_name='datamart',
            name='terms',
            field=models.ManyToManyField(blank=True, help_text='Use "ctrl" key for choose multiple terms', related_name='_datamart_terms_+', to='sample.Term', verbose_name='Terms'),
        ),
        migrations.AddField(
            model_name='book',
            name='additional_characteristics_or_marks',
            field=models.ManyToManyField(through='sample.AdditionalEntityCharacteristicOrMark', to='sample.Term'),
        ),
        migrations.AddField(
            model_name='book',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_sample.book_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='book',
            name='terms',
            field=models.ManyToManyField(blank=True, help_text='Use "ctrl" key for choose multiple terms', related_name='entities', to='sample.Term', verbose_name='Terms'),
        ),
        migrations.AddField(
            model_name='additionalentitycharacteristicormark',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.Book', verbose_name='Entity'),
        ),
        migrations.AddField(
            model_name='additionalentitycharacteristicormark',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.Term', verbose_name='Term'),
        ),
    ]
