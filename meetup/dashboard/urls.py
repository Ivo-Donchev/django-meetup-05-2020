from django.urls import path, include
from django.conf import settings
from .apis import Demo1Api, Demo2Api, Demo3Api

urlpatterns = [
    path('1/', Demo1Api.as_view()),
    path('2/', Demo2Api.as_view()),
    path('3/', Demo3Api.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
