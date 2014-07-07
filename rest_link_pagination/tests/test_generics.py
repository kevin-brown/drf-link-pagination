from rest_framework import test
from django.core.urlresolvers import reverse


class GenericsTests(test.APITestCase):

    def test_first_page(self):
        url = "%s?page=1" % (reverse("generic-list"), )

        response = self.client.get(url)

        self.assertTrue("Link" in response)

        self.assertFalse("next" in response.data)
        self.assertFalse("previous" in response.data)
        self.assertFalse("count" in response.data)

        next_link = '<http://testserver%s?page=2>; rel="next"' % (reverse("generic-list"), )

        self.assertTrue(next_link in response["Link"])
        self.assertFalse('rel="prev"' in response["Link"])

    def test_middle_page(self):
        url = "%s?page=2" % (reverse("generic-list"), )

        response = self.client.get(url)

        self.assertTrue("Link" in response)

        self.assertFalse("next" in response.data)
        self.assertFalse("previous" in response.data)
        self.assertFalse("count" in response.data)

        next_link = '<http://testserver%s?page=3>; rel="next"' % (reverse("generic-list"), )
        prev_link = '<http://testserver%s?page=1>; rel="prev"' % (reverse("generic-list"), )

        self.assertTrue(next_link in response["Link"])
        self.assertTrue(prev_link in response["Link"])

    def test_last_page(self):
        url = "%s?page=3" % (reverse("generic-list"), )

        response = self.client.get(url)

        self.assertTrue("Link" in response)

        self.assertFalse("next" in response.data)
        self.assertFalse("previous" in response.data)
        self.assertFalse("count" in response.data)

        prev_link = '<http://testserver%s?page=2>; rel="prev"' % (reverse("generic-list"), )

        self.assertTrue(prev_link in response["Link"])
        self.assertFalse('rel="next"' in response["Link"])
