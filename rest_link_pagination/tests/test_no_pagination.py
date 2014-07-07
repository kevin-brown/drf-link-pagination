from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse


class NoPagination(APITestCase):
    urls = "rest_link_pagination.tests.urls"

    def test_no_header(self):
        url = reverse("none-list")

        response = self.client.get(url)

        self.assertFalse("Link" in response)
