#encoding:utf8
import tornado.ioloop
import tornado.web
import os.path


TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	items=["Item 1","Item 2","Item 3"]
    	mapitems={'name':'Lucy','mail':'lucy@gmail.com','age':22}
    	self.render("index.html",title="My title",items=items,mapitems=mapitems)


settings = dict(
            template_path = TEMPLATE_PATH, 
            static_path = STATIC_PATH, 
            debug = True
        )


application = tornado.web.Application([
    (r"/", MainHandler),
],**settings)


if __name__ == '__main__':
	print("Server started on port:8888")
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()