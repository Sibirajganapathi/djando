from django.urls import path

from myapp1 import views
urlpatterns = [
   path('one/',views.fun),
   path('two/<x>',views.function),
   path('three/',views.admiral.as_view()),
   path('four/',views.home)
]
