import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("DeliciouSeret")


class Collector(tornado.web.RequestHandler):
    def get(self):
        # items = ["Item 1", "Item 2", "Item 3"]
        self.render("collector.html")  # , title="My title", items=items)


class getInfo(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        movie = {"id": "1", "name": "movie_name", "image":"movie_image"}
        recipe = {"id": "1", "name": "movie_name", "image":"movie_image"}
        json_dict = {"movie": movie, "recipe": recipe}
        self.finish(json.dump(json_dict, self))


class postRating(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        pass


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "login_url": "/login",
    "xsrf_cookies": True,
}

def make_app():
    return tornado.web.Application([
        (r"/", Collector),
        (r"/getInfo", getInfo),
        (r"/postRating", postRating),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
