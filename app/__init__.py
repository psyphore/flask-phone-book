from flask import Flask, jsonify, make_response, send_file, request
from flask_graphql import GraphQLView
from flask_graphql_auth import GraphQLAuth
from flask_jwt_extended import (JWTManager, jwt_required)

from app import settings
from app.graph_context import GraphContext
from app.Middleware.auth_middleware import AuthMiddleware
from app.Middleware.logger_middleware import LoggerMiddleware

from app.Routes import media_route

from .schemas import schema


def create_app():
    app = Flask(__name__)

    # add middleware to the app pipeline
    app.wsgi_app = AuthMiddleware(app.wsgi_app)
    app.wsgi_app = LoggerMiddleware(app.wsgi_app)

    # setup GraphQL Authentication and Authorization to the app pipeline
    auth = GraphQLAuth(app)
    app.config["JWT_SECRET_KEY"] = settings.JWT_SECRET_KEY
    app.config["REFRESH_EXP_LENGTH"] = settings.JWT_REFRESH_EXP_LENGTH
    app.config["ACCESS_EXP_LENGTH"] = settings.JWT_ACCESS_EXP_LENGTH

    # setup Json Web Token Manager to the app pipeline
    jwt = JWTManager(app)

    app.add_url_rule('/graphql',
                     view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=settings.DEBUG))

    @app.route('/stream/<string:name>')
    def streamed_content(name):
        return stream_content(name)

    @app.route('/media/<string:id>', defaults={'height': None, 'width': None, 'color': None})
    @app.route('/media/<string:id>/<int:height>/<int:width>', defaults={'color': None})
    @app.route('/media/<string:id>/<int:height>/<int:width>/<string:color>')
    def media(id,height,width, color):
        if color:
            return media_route.get_media(id, height=height, width=width, grey=True)

        return media_route.get_media(id, height=height, width=width, grey=False)
    
    @app.route('/media', methods=['post'])
    def process_image():
        return media_route.process_media(request.form['data'])
        

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({'message':'The request is not authenticated or unauthorized.'}), 400

    @app.errorhandler(403)
    def unauthorized(e):
        return jsonify({'message':'The request is not authenticated or unauthorized.'}), 403

    #  add global 404 handler
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'message': 'The requested URL was not found on the server.'}), 404

    @app.errorhandler(500)
    def page_not_found(e):
        return jsonify({'message': 'The Server died while processing your request.'}), 500

    return app
