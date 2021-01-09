from django.urls import path

from . import views

urlpatterns = [
    path("", views.AdvertView.as_view()),
    path("<slug:slug>/", views.AdvertDetails.as_view()),
    path("<slug:slug>/edit", views.AdvertEdit.as_view()),
    path("new",  views.AdvertCreate.as_view()),
    path("search", views.AdvertSearch.as_view()),
    path("registration" , views.NewProfile.as_view()),
    path("login", views.ProfileLogin.as_view()),
    path("logout", views.ProfileLogout.as_view()),
    path("my-adverts", views.UsersAdverts.as_view()),
]


"""
POST /

GET /login - show form
POST /login - check username and password and set cookie

GET /register - show form
POST /register - create a new user

GET /logout

GET /advert/ - list of ads
POST /advert/ - create new ad

GET /advert/11 - show details on ad #11
POST /advert/11 - update ad #11
# PATCH /advert/11
# PUT /advert/11
DELETE /advert/11 - mark ad #11 as deleted


"""
