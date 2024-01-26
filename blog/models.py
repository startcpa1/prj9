from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, verbose_name='Чпу')
    content = models.TextField(**NULLABLE, verbose_name='Описание')
    preview = models.ImageField(**NULLABLE, verbose_name='Изображение', upload_to='blog/')
    create_date = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    is_active = models.BooleanField(default=False, verbose_name='Опубликовать')
    views_count = models.IntegerField(default=0, verbose_name='Кол-во просмотров')


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


