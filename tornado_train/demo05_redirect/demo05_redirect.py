#encoding:utf8
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("You requested the main page")


class StoryHandler(tornado.web.RequestHandler):
	def get(self,story_id):
		self.write("Your requested the story "+story_id)

class BdHandler(tornado.web.RequestHandler):
	def get(self):
		self.redirect("http://www.baidu.com")

class BarHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("I am bar page")

application = tornado.web.Application([
         (r"/",MainHandler),
         (r"/story/([0-9]+)",StoryHandler),
         (r"/bd",BdHandler),
         (r"/bar",BarHandler),
         (r"/foo", 
         	tornado.web.RedirectHandler, 
         	{"url":"/bar", "permanent":False}),
         (r"/static/tornado-0.2.tar.gz", 
         	tornado.web.RedirectHandler,
         	dict(url="http://github.com/downloads/facebook/tornado/tornado-0.2.tar.gz")),
	])		


if __name__ == '__main__':
	print("Server started on port:8888")
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
