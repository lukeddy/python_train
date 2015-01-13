#encoding:utf8
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("You requested the main page")


class StoryHandler(tornado.web.RequestHandler):
	def get(self,story_id):
		path = self.request.path
		self.write("Your requested the story: "+story_id+" request path:"+path)

application = tornado.web.Application([
         (r"/",MainHandler),
         (r"/story/([0-9]+)",StoryHandler),
	])		


if __name__ == '__main__':
	print("Server started on port:8888")
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
