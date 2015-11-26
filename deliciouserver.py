import tornado.ioloop
import tornado.web
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("DeliciouSeret")


class Collector(tornado.web.RequestHandler):
    def get(self):
        # items = ["Item 1", "Item 2", "Item 3"]
        self.render("html/collector.html")  # , title="My title", items=items)


class getInfo(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        movie = {"id": "1", "name": "movie_name", "image":"movie_image"}
        recipe = {"id": "1", "name": "movie_name", "image":"movie_image"}
        json_dict = {"movie": movie, "recipe": recipe}
        self.finish(json.dump(json_dict, self))


class postRating(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        pass


def make_app():
    return tornado.web.Application([
        (r"/", Collector),
        (r"/getInfo", getInfo),
        (r"/postRating", postRating),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
