# Generated by Django 2.2.3 on 2019-08-01 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_lender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, to='book_lender.Book'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, to='book_lender.Author'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='chapters',
        ),
        migrations.AddField(
            model_name='book',
            name='chapters',
            field=models.ManyToManyField(blank=True, to='book_lender.Chapter'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='readers',
        ),
        migrations.AddField(
            model_name='book',
            name='readers',
            field=models.ManyToManyField(blank=True, to='book_lender.Reader'),
        ),
    ]
