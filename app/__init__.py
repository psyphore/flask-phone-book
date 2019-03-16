from flask import Flask, jsonify
from flask_graphql import GraphQLView
from flask_graphql_auth import GraphQLAuth

from app import settings
from app.graph_context import GraphContext

from .schemas import schema


def create_app():
    app = Flask(__name__)

    auth = GraphQLAuth(app)
    app.config["JWT_SECRET_KEY"] = settings.JWT_SECRET_KEY
    app.config["REFRESH_EXP_LENGTH"] = settings.JWT_REFRESH_EXP_LENGTH
    app.config["ACCESS_EXP_LENGTH"] = settings.JWT_ACCESS_EXP_LENGTH
    app.config["JWT_TOKEN_ARGUMENT_NAME"] = "info"

    app.add_url_rule('/graphql', 
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    
    # @app.teardown_appcontext
    # def shutdown_session(exception=None):
    #     print('> need to kill the graph_instance context')

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'message': 'The requested URL was not found on the server.'}), 404

    return app
