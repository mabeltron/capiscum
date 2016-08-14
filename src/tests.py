import os
import cap
import unittest
import tempfile

class CapTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, cap.app.config['DATABASE'] = tempfile.mkstemp
        self.app = cap.app.test_client()
        with cap.app.app_context():
            cap.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(cap.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()
