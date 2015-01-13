import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	items=["Item 1","Item 2","Item 3"]
    	mapitems={'name':'Lucy','mail':'lucy@gmail.com','age':22}
    	self.render("index.html",title="My title",items=items,mapitems=mapitems)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()