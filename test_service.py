import tornado.testing
import service


class TestFibonacciAPI(tornado.testing.AsyncHTTPTestCase):
    def get_app(self):
        return service.make_app()

    def test_fibonacci(self):
        response = self.fetch('/fibonacci/10')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body.decode(), '55')

    def test_invalid_input(self):
        response = self.fetch('/fibonacci/-1')
        self.assertEqual(response.code, 400)


if __name__ == "__main__":
    tornado.testing.main()
