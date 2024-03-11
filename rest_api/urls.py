from django.urls import path
from rest_api.views import hello_word
from rest_framework.routers import SimpleRouter
from rest_api.views import CursoModelViewSet

app_name = 'rest_api'
router = SimpleRouter(trailing_slash=False) # falso - não vai barra ao final da url
router.register('curso', CursoModelViewSet) # argumentos - prefixo e qual view

urlpatterns = [
    path('hello_word', hello_word, name='hello_world_api')
]

urlpatterns += router.urls
