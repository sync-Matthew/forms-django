from django.db.models.query import QuerySet


def suppress_django_filter_warning(get_queryset_func):
    """
    This decorator is used to fix a warning in django-filter.
    See: https://github.com/carltongibson/django-filter/issues/966
    """

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return QuerySet()
        return get_queryset_func(self)

    return get_queryset
