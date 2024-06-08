from django.db import models

from .validators import real_age

from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()


class Birthday(models.Model):
    # objects = None
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', max_length=20,
        help_text='Опциональное поле',
        blank=True
    )
    birthday = models.DateField('Дата рождения',
                                validators=(real_age,))
    image = models.ImageField('Фото',
                              upload_to='birthdays_images',
                              blank=True)
    author = models.ForeignKey(
        User, verbose_name='Автор записи',
        on_delete=models.CASCADE, null=True
    )


class Meta:
    pass

    def get_absolute_url(self):
        return reverse('birthday:detail',
                       kwargs={'pk': self.pk})
