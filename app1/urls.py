from django.urls import path

from .services.auth import sign_in, sign_up, sign_out
from .services.ishchi import get_list, delete, add, edit
from .services.mashinalar import get, addmash, editmash, delete1
from .services import users
from .views import index

urlpatterns = [

    path("", index, name="home"),
    path("ishchilar/", get_list, name="ishchi"),
    path("det/<int:pk>/", get_list, name="ishchi_det"),
    path("del/<int:pk>/", delete, name="ishchi_del"),
    path("add/", add, name="ishchi_add"),
    path("edit/<int:pk>/", edit, name="ishchi_edit"),

    path("auto/", get, name='mashina'),
    path("detmash/<int:pk>/", get, name="mashina_det"),
    path("delmash/<int:pk>/", delete1, name="mashina_del"),
    path("addmash/", addmash, name="mashina_add"),
    path("editmash/<int:pk>/", editmash, name="mashina_edit"),

    # auth
    path("login/", sign_in, name="login"),
    path("regis/", sign_up, name="regis"),
    path("logout/", sign_out, name="logout"),

    # users
    path("user_list/", users.get_list, name='user'),
    path("chp/<int:pk>/<int:status>/", users.change_perm, name='user_chp'),

]
