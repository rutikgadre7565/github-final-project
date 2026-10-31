from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)

    Talisman(
        app,
        force_https=True,
        strict_transport_security=True,
        strict_transport_security_max_age=31536000,
        content_security_policy={
            "default-src": "'self'",
            "object-src": "'none'",
            "frame-ancestors": "'none'"
        },
        referrer_policy="strict-origin-when-cross-origin"
    )

    return app
