import tornado.ioloop
import tornado.web


class FibonacciHandler(tornado.web.RequestHandler):
    def get(self, n):  
        n = int(n)
        if n < 0:
            self.set_status(400)
            self.write("N must be a non-negative integer")
            return
        self.write(str(self.fibonacci(n)))

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


def make_app():
    return tornado.web.Application([
        (r"/fibonacci/(-?[0-9]+)", FibonacciHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
