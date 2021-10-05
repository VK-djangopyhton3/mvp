from rest_framework import permissions
from django.conf import settings

from mvp.common.utils import lt_translate, is_email_valid


class UserCheckEmailOrTranslatorPermissions():
    message = "You do not have permission to perform this action."

    def has_permission(request, data):
        data.update({"email_is_valid": None, "text_translated": None})
        if request.user.groups.filter(permissions__codename="can_check_email").exists():

            """
            This is the check email is valid or not, also check user able to check email
            """
            data.update({'email_is_valid': is_email_valid(data.get('email'))})

        if request.user.groups.filter(permissions__codename="can_translate").exists():

            """
            This is the translate given words, also check user able to translate
            """
            data.update({'text_translated': lt_translate(data.get('text'), 'en', 'ja')}) # Server unavailable
            # data.update({'text_translated': data.get('text')})

        return data

