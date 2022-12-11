from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from location.models import Location
from user.validators import check_birth_date


class User(AbstractUser):
    ROLES = [
        ('member', 'Пользователь'),
        ('admin', 'Администратор'),
        ('moderator', 'Модератор'),
    ]

    role = models.CharField(max_length=9, choices=ROLES, default="member", verbose_name='Роль')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Местоположение',
                                 null=True, blank=True)
    birth_date = models.DateField(validators=[check_birth_date], verbose_name='День рождения')
    email = models.EmailField(
        unique=True, verbose_name='E-mail',
        validators=[RegexValidator(regex='@rambler.ru', inverse_match=True,
                                   message='Запрещена регистрация с почтового адреса в домене rambler.ru.')
                    ]
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username
