import tornado.ioloop
import tornado.web
import json
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("DeliciouSeret")


class Collector(tornado.web.RequestHandler):
    def get(self):
        self.render("collector.html")


class getInfo(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        movie = {"id": "1", "name": "movie_name", "image":"movie_image"}
        recipe = {"id": "1", "name": "movie_name", "image":"movie_image"}
        json_dict = {"movie": movie, "recipe": recipe}
        self.finish(json.dump(json_dict, self))


class postRate(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        the_json = json.dumps(args)
        print(the_json)
        self.write(the_json)


settings = dict(
        static_path = os.path.join(os.path.dirname(__file__), "static")
    )


def make_app():
    return tornado.web.Application([
        (r"/", Collector),
        (r"/getInfo", getInfo),
        (r"/postRate", postRate),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
