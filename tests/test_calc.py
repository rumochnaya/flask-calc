__author__ = 'scorpius'
import unittest
from flask_calc import app
import json

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_calc_get_incorrect(self):
        rv = self.app.get('/')
        assert 'The requested URL was not found on the server.' in rv.data
        self.assertTrue(rv.status_code == 404)

    def test_calc_get_correct(self):
        rv = self.app.get('/calc/')
        data = json.loads(rv.data)
        assert data == {"result": True}
        self.assertTrue(rv.status_code == 200)

    def test_calc_sum_incorrect(self):
        rv = self.app.post('/calc/sum', data=json.dumps({"one": 3, "two": 4}), content_type='application/json')
        data = json.loads(rv.data)
        assert data != {"result": 6}
        self.assertTrue(rv.status_code == 200)

    def test_calc_sum_correct(self):
        rv = self.app.post('/calc/sum', data=json.dumps({"one": 2, "two": 4}), content_type='application/json')
        data = json.loads(rv.data)
        assert data == {"result": 6}
        self.assertTrue(rv.status_code == 200)

    def test_calc_sum_incorrect_params(self):
        rv = self.app.post('/calc/sum', data='{"one": "param1", "two": 4}', content_type='application/json')
        data = json.loads(rv.data)
        self.assertTrue(rv.status_code == 400)

        rv = self.app.post('/calc/sum', data='{"one": 2, "two": "param2"}', content_type='application/json')
        data = json.loads(rv.data)
        self.assertTrue(rv.status_code == 400)
