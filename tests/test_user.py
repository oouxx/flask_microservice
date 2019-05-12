import json
from .base import BaseTestCase


class TestUserService(BaseTestCase):
    post_data = {
        'username': 'wxx',
        'email': '123@123.com'
    }

    def test_users(self):
        """确保ping的服务正常."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_user(self):
        """确保能够正确添加一个用户的用户到数据库中"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'wxx',
                    'email': '123@123.com'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('123@123.com was added', data['message'])
            self.assertEqual('success', data['status'])

    def test_add_user_invalid_json(self):
        """如果JSON对象为空，确保抛出一个错误。"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict()),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertEqual('fail', data['status'])

    def test_main_no_users(self):
        """没有用户"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('No users!', response.data.decode())

    def test_add_user_duplicate_user(self):
        """如果邮件已经存在确保抛出一个错误。"""
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps(dict(
                    username='cnych',
                    email='qikqiak@gmail.com'
                )),
                content_type='application/json'
            )
            response = self.client.post(
                '/users',
                data=json.dumps(dict(
                    username='cnych',
                    email='qikqiak@gmail.com'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Sorry. That email already exists.', data['message'])
            self.assertEqual('fail', data['status'])
