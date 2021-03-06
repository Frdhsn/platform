# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-25 11:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='datetime_from',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 25, 11, 25, 1, 340970, tzinfo=utc), verbose_name='Start datetime'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='datetime_to',
            field=models.DateTimeField(blank=True, help_text='Not required if event is on a single day', null=True, verbose_name='End datetime'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='description',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow', template='blocks/paragraph.html')), ('header', wagtail.wagtailcore.blocks.StructBlock((('header_text', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='Header', required=False)), ('size', wagtail.wagtailcore.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))), classname='title', icon='title', template='blocks/header.html')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.CharBlock(blank=True, required=False)), ('style', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('', 'Select an image size'), ('full', 'Full-width'), ('contain', 'Contained-width'), ('half', 'Half-width')], required=False))), icon='image', template='blocks/image.html')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock()), ('attribute_name', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Guy Picciotto', required=False)), ('attribute_group', wagtail.wagtailcore.blocks.CharBlock(blank=True, label='e.g. Fugazi', required=False))), icon='openquote', template='blocks/blockquote.html')), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks'))), blank=True, verbose_name='Event Description'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='summary',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
