from datetime import date
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



class VisibleAdvertsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_visible=True)


class Advert(models.Model):
    title = models.CharField("Название статьи" , max_length = 150, blank=False)
    description = models.TextField("Описание",  max_length = 150, blank=False)
    date = models.DateField("Дата объявления", default = date.today, blank=False)
    url = models.SlugField(max_length=150, unique=True)

    author = models.ForeignKey(User, verbose_name="Профиль" , on_delete=models.CASCADE,  blank=False)  # required=True

    address = models.CharField("Адрес" , max_length = 150,  blank=False)
    image = models.ImageField("Изображения", upload_to = "ads",  blank=False)
    price = models.PositiveSmallIntegerField("Цена", default = 0,  blank=False)
    status = models.CharField('Тип', choices=[('new', 'Новостройка'), ('secondhand', 'Вторичка')], max_length = 20, blank=False)
    area = models.PositiveSmallIntegerField("Площадь", default = 0,  blank=False)
    floor = models.PositiveSmallIntegerField("Этаж", default = 0,  blank=False)
    year_of_flat = models.PositiveSmallIntegerField("Год", default = 1950,  blank=False)
    city = models.CharField("Город" , max_length = 150,  blank=False)
    is_visible = models.BooleanField(default=True)

    objects = models.Manager()
    visible = VisibleAdvertsManager()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

