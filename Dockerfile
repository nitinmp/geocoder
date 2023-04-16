# Base image
# FROM python:alpine
FROM python:3

# Running every next command wih this user
USER root

# Creating work directory in docker
WORKDIR /usr/app

# Copying files to docker
ADD . '/usr/app'

# Installing Flask App
#RUN pip install flask
# RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Exposing the flask app port from container to host
EXPOSE 5000

# Starting application
CMD ["python", "app.py"]