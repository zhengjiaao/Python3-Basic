FROM python:3.10.10-slim-buster
LABEL author="zheng"
LABEL email="zhengja@gmail.com"

COPY ../../example /app
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python","main.py"]