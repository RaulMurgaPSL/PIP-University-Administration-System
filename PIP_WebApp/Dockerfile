FROM python:3.8.8
ADD . PIP_WebApp/
WORKDIR /PIP_WebApp
RUN pip install -r requirements.txt
RUN pip install pipenv
RUN pipenv install --deploy --system
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.main:app
