FROM python:3.8
COPY ./ /Flask
WORKDIR /Flask
# RUN sudo chmod a+rwx ./start.sh

RUN pip install -r requirements.txt
# RUN ls
# RUN FLASK_APP=migrate:application flask db migrate -m 'asd'
# RUN FLASK_APP=migrate:application flask db upgrade
CMD ["python", "run.py"]
# CMD ["start.sh"]
# ENTRYPOINT ["./start.sh"]
