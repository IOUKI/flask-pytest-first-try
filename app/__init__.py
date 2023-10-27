from flask import Flask

def createApp():
    app = Flask(__name__)
    
    from app.apiRoute.test import router as TestRouter
    app.register_blueprint(TestRouter, url_prefix='/')

    return app