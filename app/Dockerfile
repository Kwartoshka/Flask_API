FROM python:3.8
COPY ./ /Flask
WORKDIR /Flask
RUN pip install -r requirements.txt
# RUN FLASK_APP=migrate:application flask db upgrade
CMD ["python", "run.py"]

