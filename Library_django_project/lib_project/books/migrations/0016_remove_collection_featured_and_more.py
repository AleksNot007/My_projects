# Generated by Django 5.2 on 2025-06-10 11:16

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_author_wiki_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='views_count',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='chapter',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='likes',
        ),
        migrations.AddField(
            model_name='userbookrelation',
            name='is_favourite',
            field=models.BooleanField(default=False, verbose_name='В избранном'),
        ),
        migrations.AddField(
            model_name='userbookrelation',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Личные заметки'),
        ),
        migrations.AddField(
            model_name='userbookrelation',
            name='progress',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Процент прочитанного'),
        ),
        migrations.AddField(
            model_name='userbookrelation',
            name='progress_pages',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество прочитанных страниц'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='books',
            field=models.ManyToManyField(db_column='book_id', related_name='collections', to='books.book', verbose_name='Книги'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collections', to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='is_public',
            field=models.BooleanField(default=True, help_text='Если отмечено, подборка будет видна всем пользователям', verbose_name='Публичная'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='slug',
            field=models.SlugField(help_text='Уникальный идентификатор для URL', unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='is_public',
            field=models.BooleanField(default=True, help_text='Если отмечено, цитата будет видна на странице книги', verbose_name='Публичная цитата'),
        ),
        migrations.AlterField(
            model_name='userbookrelation',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_relations', to='books.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='userbookrelation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_relations', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=models.Index(fields=['created_by', 'is_public'], name='books_colle_created_b22452_idx'),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=models.Index(fields=['type', 'created_at'], name='books_colle_type_870ee6_idx'),
        ),
        migrations.AddIndex(
            model_name='quote',
            index=models.Index(fields=['book', 'is_public'], name='books_quote_book_id_9385df_idx'),
        ),
        migrations.AddIndex(
            model_name='quote',
            index=models.Index(fields=['user', 'created_at'], name='books_quote_user_id_aa384c_idx'),
        ),
    ]
