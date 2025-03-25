from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.login_view,name='register'),
    path('reg',views.index ,name="index"),
    path('cake_upld',views.cake_upld,name="cake_upld"),
    path('cakeview',views.cake_view_all,name="cakeview"),
    path('viewcart',views.viewcart,name='viewcart'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('cartdel',views.cartdel,name='cartdel'),
    path('home',views.home,name="home"),
    path('choco_mail',views.choco_mail)
    

   
]