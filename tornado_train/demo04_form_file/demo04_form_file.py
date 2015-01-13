#encoding:utf8
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		#self.write("You requested the main page")
		self.write('<html><body><form action="/" method="post" enctype="multipart/form-data">'
                   '<p>Message:<input type="text" name="message"></p>'
                   '<p>File:<input type="file" name="file"></p>'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

	def post(self):
    	 self.set_header("Content-Type","text/plain")
    	 uploadedfile=self.request.files['file']
    	 self.write("You wrote: "+self.get_argument("message")+" file name:"+uploadedfile[0]['filename'])


application = tornado.web.Application([
         (r"/",MainHandler),
	])		


if __name__ == '__main__':
	print("Server started on port:8888")
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()