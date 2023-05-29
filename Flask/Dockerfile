FROM python:3.10.1
COPY requirements.txt requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt
COPY ./src/web_con_flask.py /src/web_con_flask.py
EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["/src/web_con_flask.py"]