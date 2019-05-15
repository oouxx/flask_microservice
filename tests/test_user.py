import json
from tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    def test_users(self):
        """确保ping的服务正常."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_user(self):
        """确保能够正确添加一个用户的用户到数据库中"""
        with self.client:
            response = self.client.post(
                '/login',
                data={'username': 'wxx', 'email': 'test@qq.com', 'password': 'password'},
            )
            # print(response.data)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('success', data['message'])
            self.assertEqual('success', data['status'])

    def test_add_user_invalid_json(self):
        """如果JSON对象为空，确保抛出一个错误。"""
        with self.client:
            response = self.client.post(
                '/login',
                data=None,
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertEqual('fail', data['status'])
