Install pip:
apt-get update
apt install python3-pip

To install requirements:
pip install gunicorn flask flask_cors flask_restful
apt install gunicorn

To clone code:
git clone https://github.com/billyParmenter/BasicFlaskServer.git

To run:
gunicorn --config gunicorn_config.py app:app