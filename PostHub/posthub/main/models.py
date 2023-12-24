from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from datetime import datetime

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


User = get_user_model()

class dnld(models.Model):
    '''Данные о статье'''
    title = models.CharField('Заголовок статьи', max_length=100)
    text = models.TextField('Текст статьи')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    img = models.ImageField('изображение', upload_to='image/%Y')
    created_at = models.DateTimeField('Дата создания', default=datetime.now)

    def __str__(self):
        return f'{self.title} ({self.created_at})'

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'


@receiver(pre_save, sender=dnld)
def set_author(sender, instance, **kwargs):
    if not instance.author_id:
        instance.author = User.objects.get(username='username')  # Replace 'username' with your desired default username

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'object_id', 'content_type'],
                name='unique_user_content_type_object_id'
            )
        ]