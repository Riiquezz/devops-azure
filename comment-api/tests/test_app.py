import unittest
from app import app

class CommentApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_comment(self):
        response = self.app.post('/api/comment/new', json={
            'email': 'test@example.com',
            'comment': 'This is a test comment',
            'content_id': 1
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Comment created successfully', str(response.data))

    def test_list_comments(self):
        response = self.app.get('/api/comment/list/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
