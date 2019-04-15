from django.urls import path, include
from . import views
from tastypie.api import Api
from .api import JobResource

v_1_api = Api(api_name='v1')
v_1_api.register(JobResource())

urlpatterns = [
    # path('', views.HomePageView.as_view(), name='home'),
    path('', include(v_1_api.urls)),
]
