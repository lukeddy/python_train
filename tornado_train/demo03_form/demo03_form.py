#encoding:utf8
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		#self.write("You requested the main page")
		self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

	def post(self):
    	 self.set_header("Content-Type","text/plain")
    	 self.write("You wrote "+self.get_argument("message"))


application = tornado.web.Application([
         (r"/",MainHandler),
	])		


if __name__ == '__main__':
	print("Server started on port:8888")
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
