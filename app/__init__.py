from flask import Flask, jsonify
from flask_graphql import GraphQLView

from app.graph_context import GraphContext


from .schemas import schema


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/graphql', 
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True, context={'db_session': GraphContext.get_instance_2}))

    # @app.teardown_appcontext
    # def shutdown_session(exception=None):
    #     print('> need to kill the graph_instance context')

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'message': 'The requested URL was not found on the server.'}), 404

    return app
