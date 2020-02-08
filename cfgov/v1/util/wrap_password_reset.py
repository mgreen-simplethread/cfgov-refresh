from functools import wraps

from django.http import Http404

from wagtail.admin.views import account


def _wrap_password_reset_view(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if not account.password_reset_enabled():
            raise Http404
        return view_func(*args, **kwargs)
    return wrapper
