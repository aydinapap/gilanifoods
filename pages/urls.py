from django.urls import path
from .import views

urlpatterns = [
    #home url
    path('',views.HomePageView.as_view(),name="home"),
    #about url
    path('about/',views.AboutPageView.as_view(),name="about"),
    #
    path('postview/',views.PostListView.as_view(),name="پست"),
    path('اردک واویشکا',views.OrdakVavishkaPageView.as_view(),name="اردک واویشکا"),
    path('انار بیج',views.AnarBijPageView.as_view(),name="انار بیج"),
    path('باقالی قاتوق',views.BaghaliGhatoghPageView.as_view(),name="باقالی قاتوق"),
    path('ترش تره',views.TorshTarePageView.as_view(),name="ترش تره"),
    path('جغول مغول',views.JagholMagholPageView.as_view(),name="جغول مغول"),
    path('سیر قلیه',views.SirGhaliyePageView.as_view(),name="سیر قلیه"),
    path('فسنجون',views.FesenjoonPageView.as_view(),name="فسنجون"),
    path('کال کباب',views.KalKababPageView.as_view(),name="کال کباب"),
    path('میرزا قاسمی',views.MirzaGhasemiPageView.as_view(),name="میرزا قاسمی"),
]