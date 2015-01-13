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
    	 if not self.get_cookie("mycookie"):
            self.set_cookie("mycookie", msg)
            self.write("Your cookie was not set yet!")
    	 else:

            self.write("Your cookie was set! Value is :"+str(self.get_cookie("mycookie")))


application = tornado.web.Application([
         (r"/",MainHandler),
	])		


if __name__ == '__main__':
	print("Server started on port:8888")
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
