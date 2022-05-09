FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# tr_TR.UTF-8 UTF-8/tr_TR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

ENV LANG tr_TR.UTF-8
ENV LC_ALL tr_TR.UTF-8
ENTRYPOINT ["python"]
CMD ["main.py"]