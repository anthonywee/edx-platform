# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from opaque_keys.edx.django.models import CourseKeyField


class Migration(migrations.Migration):

    dependencies = [
        ('django_comment_common', '0004_auto_20161117_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDiscussionSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_id', CourseKeyField(help_text=b'Which course are these settings associated with?', unique=True, max_length=255, db_index=True)),
                ('always_divide_inline_discussions', models.BooleanField(default=False)),
                ('_divided_discussions', models.TextField(null=True, db_column=b'divided_discussions', blank=True)),
                ('division_scheme', models.CharField(default=b'none', max_length=20, choices=[(b'none', b'None'), (b'cohort', b'Cohort'), (b'enrollment_track', b'Enrollment Track')])),
            ],
            options={
                'db_table': 'django_comment_common_coursediscussionsettings',
            },
        ),
    ]
