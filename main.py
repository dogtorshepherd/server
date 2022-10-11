from os.path import dirname, join

from flask import Flask
from flask_cors import CORS
from flask_json_schema import JsonSchema
from dotenv import load_dotenv
from routers import router

dotenv_path = join(dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)

def create_app() :
    schema = JsonSchema()
    app = Flask(__name__)
    CORS(app)
    app.config['SWAGGER'] = {
        'title': 'Flask API SQL SYSTEM',
    }
    app.config["JSON_SORT_KEYS"] = False

    schema.init_app(app)
    router(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)