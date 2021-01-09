from datetime import date
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# class Profile(User):
#     # name = models.CharField("Имя профиля" , max_length = 150,  blank=False)
#     # registration_date = models.models.DataField("Дата регистрации", default = date.today)
#     # email = models.EmailField(blank=False) C:\notcian>dev\Scripts\activate
#     phone_number = models.PositiveSmallIntegerField("Номер телефона", default = 0,  blank=False)  # !
#     url = models.SlugField(max_length = 160, unique = True)  # !
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Профиль"

class VisibleAdvertsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_visible=True)


class Advert(models.Model):
    title = models.CharField("Название статьи" , max_length = 150, blank=False)
    description = models.TextField("Описание",  max_length = 150, blank=False)
    date = models.DateField("Дата объявления", default = date.today, blank=False)
    url = models.SlugField(max_length=150, unique=True)

    author = models.ForeignKey(User, verbose_name="Профиль" , on_delete=models.CASCADE,  blank=False)  # required=True
    # agents = models.ManyToManyField(User, verbose_name="Агенты")
    # number = models.ForeignKey(Profile, verbose_name = "Номер телефона", on_delete = models.CASCADE,  blank=False)

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

"""
Users
-------------
id | username
-------------
1  | filipp
2  | ivan
3  | cristina
4  | valeria
-------------

user 1 - many ads
--------------------
id | user_id | title | ...
--------------------
1  | 1       | Красочная квартира-студия в центре Казани
2  | 1       | Доступная квартира у парка
3  | 2       | Просторная квартира не далеко от моря

user many - ads many
--------------------
id | user_id | ad_id
--------------------
1  | 3       | 1
2  | 3       | 2
3  | 3       | 3
4  | 4       | 1
5  | 4       | 2
--------------------
"""

"""
class List_ad(models.Model):
    list_ad_title = models.ForeignKey(main_ad, verbose_name = "Название",on_delete = models.CASCADE)
    list_adress = models.ForeignKey(main_ad, verbose_name = "Адрес",on_delete = models.CASCADE)
    list_name_profile = models.ForeignKey(main_ad, verbose_name = "Профиль",on_delete = models.CASCADE)
    list_image_ad = models.ForeignKey (main_ad, verbose_name = "Изображения",on_delete = models.CASCADE)
    list_price_ad = models.ForeignKey(main_ad, verbose_name = "Цена",on_delete = models.CASCADE)
    list_description = models.ForeignKey(main_ad, verbose_name = "Описание",on_delete = models.CASCADE)
    list_number = models.ForeignKey(main_ad, verbose_name = "Номер",on_delete = models.CASCADE)
    list_date_ad = models.ForeignKey(main_ad, verbose_name = "Дата",on_delete = models.CASCADE)
    url = models.SlugField(max_length = 160, unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
"""
