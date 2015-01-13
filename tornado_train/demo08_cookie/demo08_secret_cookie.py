#encoding:utf8
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		#self.write("You requested the main page")
		self.write('<html><body><form action="/" method="post">'
                   'Cookie Value:<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

	def post(self):
    	 self.set_header("Content-Type","text/plain")
    	 msg=self.get_argument("message")
    	 if not self.get_secure_cookie("mycookie2"):
            self.set_secure_cookie("mycookie2", msg)
            self.write("Your cookie was not set yet!")
    	 else:
            #cookieValue=self.get_secure_cookie("mycookie2").decode("utf-8")
            cookieValue=str(self.get_secure_cookie("mycookie2"),encoding="utf-8")
            print(cookieValue)
            #中文输出需要设置编码，否则会出乱码
            self.set_header("Content-Type","text/plain;charset=utf-8")
            self.write("Your cookie was set!"+cookieValue)


application = tornado.web.Application([
         (r"/",MainHandler),
	],cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")		


if __name__ == '__main__':
	print("Server started on port:8888")
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
