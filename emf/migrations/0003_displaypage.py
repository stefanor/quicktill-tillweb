# Generated by Django 3.2.13 on 2022-05-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emf', '0002_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Internal name for the display. If multiple pages of the same priority are being displayed, they will be shown in alphanumeric order by name.', max_length=80, unique=True)),
                ('display_after', models.DateTimeField(blank=True, help_text="Don't display this page until after this time", null=True)),
                ('display_until', models.DateTimeField(blank=True, help_text='Stop displaying this page after this time', null=True)),
                ('display_time', models.IntegerField(default=30, help_text='Display the page for this number of seconds')),
                ('priority', models.CharField(choices=[('U', 'Urgent'), ('N', 'Normal'), ('L', 'Low')], help_text='Priority for this page. Urgent pages suppress the display of all other pages; normal pages appear first in the list of pages, low priority pages appear last in the list.', max_length=1)),
                ('title', models.CharField(blank=True, help_text='Title to be shown at the top of the display, between the logo and the clock', max_length=80)),
                ('content', models.TextField(help_text='Content for the page. Markdown or HTML.')),
            ],
        ),
    ]