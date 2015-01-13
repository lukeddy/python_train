#encoding:utf-8
import tornado.ioloop
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render("main.html",username=name)

class LoginHandler(BaseHandler):
    def get(self):
        self.render("form.html")

    def post(self):
        self.set_secure_cookie("username", self.get_argument("username"))
        self.redirect("/")


settings = {
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": True,
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
], **settings)


if __name__ == '__main__':
	print("Server started on port:8888")
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()