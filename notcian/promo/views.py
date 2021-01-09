from django.shortcuts import render, redirect
from django.views.generic.base import View
# Create your views here.
from promo.models import Advert
from promo.forms import AdvertForm, ProfileForm, AuthProfileForm
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.http import Http404


class AdvertView(View):
    """Список всех объявлений"""
    def get(self, request):
        adverts = Advert.visible.all()  # TODO: use custom manager
        return render(request, "adverts/adverts_list.html" , {"advert_list": adverts})


class AdvertDetails(View):
    """Одно полное объявление"""
    def get(self, request, slug):
        advert = Advert.visible.get(url = slug)
        user = request.user # TODO: check ad's visibility
        author_is_user = False
        if user == advert.author:
            author_is_user = True
        data = {"advert": advert, "author_is_user": author_is_user}
        return render(request, "adverts/advert.html" , data)

    def post(self, request, slug):
        # TODO: check if user owns the advert
        advert = Advert.visible.get(url=slug)
        if advert.author != request.user or not request.user.is_authenticated:
              raise Http404("No permissions")# TODO: repeated deletion
        action = request.POST['action']
        if action == "hide":
            advert.is_visible = False
        else:
            advert.is_visible = True  # TODO: a better name
        advert.save()
        return redirect("/")


class AdvertEdit(View):
    def get(self, request, slug):
        advert = Advert.visible.get(url=slug)  # TODO: check ad is visible
        if advert.author != request.user or not request.user.is_authenticated:
            raise Http404("No permissions")
        initial = {'title':advert.title,'description':advert.description, 'date':advert.date, 'url':advert.url, 'author':advert.author, 'address':advert.address,'image':advert.image, 'price':advert.price, 'status':advert.status, 'area':advert.area, 'floor':advert.floor, 'year_of_flat':advert.year_of_flat, 'city':advert.city}
        form = AdvertForm(initial=initial)
        data = {'form': form}
        return render(request, "adverts/advert_edit.html" , data)

    def post(self, request, slug):
        advert = Advert.visible.get(url=slug)  # TODO: check visibility
        if advert.author != request.user or not request.user.is_authenticated:
            raise Http404("No permissions")
        form = AdvertForm(request.POST,request.FILES, instance = advert)
        error = form.errors.as_data()
        if form.is_valid():
            form.save()
            return redirect("/")
        er = {'error': error}
        return render(request, 'adverts/advert_edit.html', er)


def translate_title(title):
    alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya', ' ': '-'}
    result_title = ""
    for char in title.lower():
        if char in alphabet:
            result_title += alphabet[char]
        else:
            result_title +=char
    return result_title

class AdvertCreate(View):
    def get(self,request):
        if not request.user.is_authenticated:
            raise Http404("Please log in")
        error = ''
        form = AdvertForm()
        data = {'form' : form, 'error': error}
        return render(request, 'adverts/add_adverts.html', data)


    def post(self ,request):
        if not request.user.is_authenticated:
            raise Http404("Please log in")
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            advert = form.save(commit=False)
            advert.url = translate_title(advert.title)
            advert.author = request.user
            advert.is_visible = True
            advert.save()
            # TODO: django messages
            return redirect("/")
        error = form.errors.as_data()
        data = {'form' : form, 'error': error}
        return render(request, 'adverts/add_adverts.html', data)

    



class AdvertSearch(View):
    def post(self, request):
        query = request.POST['query']
        filter_expr = Q()
        for word in query.split(' '):
            filter_expr |= Q(title__icontains=word) | Q(description__icontains=word) | Q(city__icontains=word)
        qs = Advert.visible.filter(filter_expr)
        return render(request, "adverts/adverts_list.html" , {"advert_list": qs, "query": query})


# class ProfileLogin(LoginView):
#     def get(self, request):
#         form = AuthProfileForm()
#         data = {'form' : form}
#         return render(request, 'adverts/auth.html', data)
#
#     def post(self,request):
#         form = AuthProfileForm(request.POST)
#

class ProfileLogin(View):
    def get(self, request):
         form = AuthProfileForm()
         data = {'form' : form}
         return render(request, 'adverts/auth.html', data)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user and user.is_active:
            login(request, user)
            return redirect("/")

        form = AuthProfileForm(request.POST)
        error = "The username or password were incorrect"
        data = {'error': error, 'form' : form}
        return render(request, 'adverts/auth.html', data)


class ProfileLogout(View):
     def get(self, request):
         logout(request)  # what if the user is not logged in?
         return redirect("/")


class NewProfile(View):
    def get(self, request):
        form = ProfileForm()
        data = {'form' : form}
        return render(request, 'adverts/registration.html', data)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # TODO: put a message
            form.save()
        else:
            pass
        return redirect("/")


class UsersAdverts(View):
    def get(self, request):
        if not request.user.is_authenticated:
            raise Http404("Please log in")
        adverts = Advert.visible.filter(author=request.user)
        return render(request, "adverts/users_advert.html" , {"advert_list": adverts})
