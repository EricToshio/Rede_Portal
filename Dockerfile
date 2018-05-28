 FROM python:3.6.5
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /Rede_Portal
 WORKDIR /Rede_Portal
 ADD requirements.txt /Rede_Portal/
 RUN pip install -r requirements.txt
 ADD . /Rede_Portal/
 EXPOSE 8000