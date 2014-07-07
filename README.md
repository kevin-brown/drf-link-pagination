DRF Link Pagination
===================
By default Django REST Framework provides pagination information within the body
of a response.

While this has been [addressed in the past][drf-1169], the general consensus has
been to make a third-party package until the pagination can be refactored in the
DRF core.  Until the refactoring happens, this package provides a very basic
implementation of the [`Link` header][rfc-link] for pagination.

How do I use this?
==================
When creating your generic view or viewset, you need to include the
`LinkPaginationMixin` towards the beginning.  You will also need to set up
[pagination][pagination] on the view using the default pagination serializer.

```python
from rest_framework import viewsets
from rest_link_pagination import mixins

from example.models import ExampleModel
from example.serializers import ExampleSerializer


class ExampleViewSet(mixins.LinkPaginationMixin, viewsets.ModelViewSet):
    queryset = ExampleModel.objects.all()
    serializer_class = ExampleSerializer
    paginate_by = 25
```

When you make a request to your API, it will return the pagination data in the
`Link` header instead of within the body of the response.  The response will be
returned as an array instead of an object with the key `results`, similar to an
unpaginated response.

```http
Link: <http://testserver/generic/list?page=2>; rel="next"
Content-Type: application/json
Allow: GET, HEAD, OPTIONS
Vary: Accept, Cookie

[{"id": 1, "name": "example"}, ...]
```

Tests
=====
The tests can be run through your Django app by running:

    python manage.py test rest_link_pagination

or within the project by running:

    python rest_link_pagination/tests/run.py

Contributing
============
If you see something that needs to be fixed, send us a pull request. If you
don't feel like fixing it, or are not sure how to go about it,
[create an issue][new-issue] on GitHub about it and we can work it out.

The issue tracker is available [on GitHub][issues].

[drf-1169]: https://github.com/tomchristie/django-rest-framework/issues/1169
[issues]: https://github.com/kevin-brown/drf-link-pagination/issues
[new-issue]: https://github.com/kevin-brown/drf-link-pagination/issues/new
[pagination]: http://www.django-rest-framework.org/api-guide/pagination#pagination-in-the-generic-views
[rfc-link]: http://tools.ietf.org/html/rfc5988
