FROM python:3
RUN pip install gunicorn flask blinker flask-sso
COPY ssotutorial /ssotutorial
WORKDIR /ssotutorial
EXPOSE 8000

