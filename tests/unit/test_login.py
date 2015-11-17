# -*- encode utf-8 -*-
from . import BaseTestCase


class TestLoginCase(BaseTestCase):

    def first_test(self):
        self.assertEqual(1, 1)

    def test_register(self):
        rv = self.app.get('/register/')
        self.assertEqual(rv.status_code, 200)

    def test_login(self):
        rv = self.app.get('/login/')
        self.assertEqual(rv.status_code, 200)
