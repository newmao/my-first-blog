from django.conf import settings
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (
        url(r'^your_app/', include(debug_toolbar.urls)),
    )