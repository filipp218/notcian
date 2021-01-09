from django.forms import ModelForm
from promo.models import Advert
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        exclude = ['url', 'author']
        #fields = ['title', 'description', 'date', 'address','image', 'price', 'status', 'area', 'floor', 'year_of_flat', 'city']

class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class AuthProfileForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        # widgets = {
        #     "title" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Название'}),
        #     "description" : Textarea(attrs ={'class': 'form-control', 'placeholder': 'Описание'}),
        #     "date" : DateTimeInput(attrs ={'class': 'form-control', 'placeholder': 'Дата'}),
        #     "url" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'ЮРЛ'}),
        #     "address" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Адрес'}),
        #     "city" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Город'})
        # }
        #
        #     "author" : ??  (attrs ={'class': 'form-control', 'placeholder': 'Ваше имя'}),
        #     "image" : ??  (attrs ={'class': 'form-control', 'placeholder': 'Изображение'}),
        #     "price" : ??  (attrs ={'class': 'form-control', 'placeholder': 'Цена'}),
        #     "status" : ??  (attrs ={'class': 'form-control', 'placeholder': 'Статус'}),
        #     "area" : ??  (attrs ={'class': 'form-control', 'placeholder': 'Площадь'}),
        #     "floor" : ??  (attrs ={'class': 'form-control', 'placeholder': 'Этаж'}),
        #     "year_of_flat" : ??  (attrs ={'class': 'form-control', 'placeholder': 'Год постройки'}),



#
# def get(self, request):
#     return render(request, "adverts/add_adverts.html", {'advert_form': fields})


# class AdvertForm(forms.Form):
#     title = forms.CharField( max_length = 150)
#     description = forms.CharField( max_length = 150)
#     url = forms.SlugField(max_length = 160, unique = True)
#
#     author = models.ForeignKey(User, verbose_name="Профиль" , on_delete=models.CASCADE,  blank=False)  # required=True
#     # agents = models.ManyToManyField(User, verbose_name="Агенты")
#     # number = models.ForeignKey(Profile, verbose_name = "Номер телефона", on_delete = models.CASCADE,  blank=False)
#
#     address = forms.CharField("Адрес" , max_length = 150,  blank=False)
#     image = forms.ImageField("Изображения", upload_to = "ads",  blank=False)
#     price = forms.PositiveSmallIntegerField("Цена", default = 0,  blank=False)
#     status = forms.CharField('Тип', choices=[('new', 'Новостройка'), ('secondhand', 'Вторичка')], max_length = 20, blank=False)
#     area = forms.PositiveSmallIntegerField("Площадь", default = 0,  blank=False)
#     floor = forms.PositiveSmallIntegerField("Этаж", default = 0,  blank=False)
#     year_of_flat = forms.PositiveSmallIntegerField("Год", default = 1950,  blank=False)
#     city = forms.CharField("Город" , max_length = 150,  blank=False)
#
#     def clean_url(self):
#         new_url = self.cleaned_data['url'].lower()
#
#         if new_url == 'create':
#             raise ValidationError('Url cant be create')
#         return new_url
#
#     def save(self):
#         new_advert = Advert.objects.create(title = self.cleaned_data['title'], description = self.cleaned_data['description'], date = self.cleaned_data['date'], url = self.cleaned_data['url'], author = self.cleaned_data['author'], adress = self.cleaned_data['adress'], image = self.cleaned_data['image'], price = self.cleaned_data['price'],status = self.cleaned_data['status'],area = self.cleaned_data['area'],floor = self.cleaned_data['floor'], year_of_flat = self.cleaned_data['year_of_flat'], city = self.cleaned_data['city'] )
#         return new_advert
            #
            #
            # "title" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Название'}),
            # "description" : Textarea(attrs ={'class': 'form-control', 'placeholder': 'Описание'}),
            # "date" : DateTimeInput(attrs ={'class': 'form-control', 'placeholder': 'Дата'}),
            # "url" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'ЮРЛ'}),
            # "author" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            # "address" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Адрес'}),
            # "image" : ImageField(attrs ={'class': 'form-control', 'placeholder': 'Изображение'}),
            # "price" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Цена'}),
            # "status" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Статус'}),
            # "area" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Площадь'}),
            # "floor" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Этаж'}),
            # "year_of_flat" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Год постройки'}),
            # "city" : TextInput(attrs ={'class': 'form-control', 'placeholder': 'Город'})
