from django.urls import path
from .views import SomeView
from django.conf.urls import url

urlpatterns = [
    url(r'^1dc3b3632d3f29976dac279ca041e8f0413ac188eb24aa670d/?$', SomeView.as_view())
]