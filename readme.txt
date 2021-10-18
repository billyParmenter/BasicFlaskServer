To install requirements:
pip install gunicorn flask flask_cors flask_restful

To run:
gunicorn --config gunicorn_config.py app:app