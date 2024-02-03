

import requests
import unittest


class ApiTest(unittest.TestCase):
    def test_verify_mail_de_post(self):
        req = requests.get("https://jsonplaceholder.typicode.com/comments?postId=2")
        result = req.json()
        self.assertTrue('Presley.Mueller@myrl.com' == result[0]['email'], msg="El email no coincide.")
        self.longMessage = True

    def test_verify_id(self):
        req = requests.get("https://jsonplaceholder.typicode.com/comments?postId=2")
        result = req.json()
        self.assertTrue(6 == result[0]['id'], msg="El ID no coincide.")
        self.longMessage = True


if __name__ == '__main__':
    unittest.main()
