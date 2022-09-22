# Generated by Django 4.1.1 on 2022-09-22 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('book_author', models.CharField(max_length=50)),
                ('books_quantity', models.IntegerField()),
                ('books_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BooksCategory', to='app.bookscategory')),
            ],
        ),
    ]
