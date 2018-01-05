from django.urls import include, path


urlpatterns = [
    path('podcasts/', include('podcast.urls')),
]