from environs import Env


env = Env()


DEBUG = env.bool('DEBUG', default=False)
BIND_HOST = env('BIND_HOST', default='127.0.0.1')
BIND_PORT = env.int('BIND_PORT', default=5000)

NEO4J_URI = env('NEO4J_URI', default='bolt://localhost:7687')
NEO4J_USER = env('NEO4J_USER', default='neo4j')
NEO4J_PASSWORD = env('NEO4J_PASSWORD', default='n4j')

JWT_SECRET_KEY= env('JWT_SECRET_KEY', default='super secret key')
JWT_REFRESH_EXP_LENGTH = env.int('JWT_REFRESH_EXP_LENGTH',default=30)
JWT_ACCESS_EXP_LENGTH = env.int('JWT_ACCESS_EXP_LENGTH', default=10)
JWT_TOKEN_ARGUMENT_NAME = env('JWT_TOKEN_ARGUMENT_NAME', default='token')
