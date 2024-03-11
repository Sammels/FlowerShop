from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from flower_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('card/', views.card, name='card'),
    path('catalog/', views.catalog, name='catalog'),
    path('consultation/', views.consultation, name='consultation'),
    path('order-step/', views.order_step, name='order-step'),
    path('order/', views.order, name='order'),
    path('quiz-step/', views.quiz_step, name='quiz-step'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
