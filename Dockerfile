FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y locales locales-all
ENV LC_ALL tr_TR.UTF-8
ENV LANG tr_TR.UTF-8
ENV LANGUAGE tr_TR.UTF-8
ENTRYPOINT ["python"]
CMD ["main.py"]