from rest_framework.response import Response


def return_response(data, success, message, status):
    """This method for custom response"""
    try:
        if not success and message == 'Bad request!':
            data_keys = list(data.keys())
            message = "".join(data[data_keys[0]])
    except Exception as e:
        pass

    response_data = {"data":data, "success": success, "message": message, 'status': status}
    return Response(response_data, status=status)


def lt_translate(text, source_language=None, target_language=None):
    """This method is use for translation"""
    try:

        from libretranslatepy import LibreTranslateAPI
        lt = LibreTranslateAPI("https://translate.astian.org/")

        if not source_language:
            source_language = lt.detect(text)[0].get('language', None) # We can detect language but HTTP Error 503: Service Unavailable

        if not target_language:
            target_language = 'en'
        text = lt.translate(text, target_language, source_language)
    except Exception as e:
        text = text
    return text


def is_email_valid(email):
    """This method is use for check email exists or valid"""
    from email_validate import validate, validate_or_fail
    is_valid = validate(email_address=email, check_format=True, check_blacklist=True, check_dns=True, dns_timeout=10, check_smtp= False, smtp_debug=False)
    return is_valid
