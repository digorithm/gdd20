# -*- encode utf-8 -*-
from . import BaseTestCase


class TestRescipes(BaseTestCase):

    def first_test(self):
        self.assertEqual(1, 1)

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)

    def test_url_not_found(self):
        rv = self.app.get("/recipes/items")
        self.assertEqual(rv.status_code, 404)

    def test_result_search(self):
        rv = self.app.post('/recipes/', data=dict(items=''))
        self.assertEqual(rv.status_code, 302)
        rv = self.app.post('/recipes/', data=dict(items='feijao,carne,ovo'))
        self.assertEqual(rv.status_code, 500)
        rv = self.app.post('/recipes/', data=dict(items='arroz,carne'))
        self.assertEqual(rv.status_code, 200)
