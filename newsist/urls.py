from django.urls import path
from .views import (GetAllNewsView,  PlaceNewsView, CategoryNewsView, GetOneNewsView,)
                    # GetOneAdmin,  PostOneAdmin, PalceGetAdmin, GetAdminCategoryView,PostNewsView,
                    # LoginView)

urlpatterns = [
    path('getallnews/<str:language>/', GetAllNewsView.as_view()), # for get all news
    # path('postnews/', PostNewsView.as_view()),     # for post new news
    path('placenews/', PlaceNewsView.as_view()),    # for get news via place
    path('categorynews/', CategoryNewsView.as_view()), # for get news via category
    path('getonenews/', GetOneNewsView.as_view()),      # for get one news
    # path('getoneadmin/', GetOneAdmin.as_view()),    # for get one admin via name
    # path('postoneadmin/', PostOneAdmin.as_view()),   # for post new admin
    # path('placeadmin/', PalceGetAdmin.as_view()),   # for get one admin via place
    # path('admincategory/', GetAdminCategoryView.as_view()), # for get admin via category
    # path('login/', LoginView.as_view()), # for login of workers
]