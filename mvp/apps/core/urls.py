from django.urls import path

from mvp.apps.core.views import EmailCheckAndTranslatorAPIView

app_name='core'
urlpatterns = [
    path('check/', EmailCheckAndTranslatorAPIView.as_view(), name='email_check_or_translator'),
]