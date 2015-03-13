from django.conf.urls import patterns, url

from tokenapi.views import token
from tokenapi.views import token_new
from tokenapi.views import validate_json


urlpatterns = [
    url(r'^token/new.json$', token_new, name='api_token_new'),
    url(r'^token/(?P<token>.{24})/(?P<user>\d+).json$', token, name='api_token'),
    url(r'^token/validate.json$', validate_json, name='validate_json'),
]
