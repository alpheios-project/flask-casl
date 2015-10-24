from flask import request, Blueprint, abort, send_from_directory

class Casl(object):

    def __init__(self, prefix="/casl", name=None, app=None):
        self.name = name
        self.prefix = prefix
        self.app = app

        if not name:
            self.name = __name__
        
        self.routes = [("/word/<word>", "r_word", ["GET"])]

        if self.app is not None:
            self.init_app(app)



    def init_app(self, app):
        """ Register the blueprint to the app
        :param app: Flask Application
        :return: Blueprint for Casl registered in app
        :rtype: Blueprint
        """
        self.blueprint = Blueprint(
            self.name,
            self.name,
            url_prefix=self.prefix,
        )

        for url, name, methods in self.routes:
            self.blueprint.add_url_rule(
                url,
                view_func=getattr(self, name),
                endpoint=name,
                methods=methods
            )

        self.app.register_blueprint(self.blueprint)
        return self.blueprint


    def register_routes(self):
        """ Register routes on app using Blueprint
        :return: FlaskCasl blueprint
        :rtype: flask.Blueprint
        """
        if self.app is not None:
            if not self.blueprint:
                self.blueprint = self.create_blueprint()
            self.app.register_blueprint(self.blueprint)
            return self.blueprint
        return None

    def r_word(self,word):
        response = self.parse(word)
        return response, 200, { "Content-Type": "application/xml"}


    def parse(self, word):
        return "<word>" + word + "</word>"

if __name__ == "__main__":
    run()
