# creating a Dockerfile to be used for building the container

# Step 1: I need a base image to use for my file
FROM python:3.7.3-stretch

# copying in the requirements.txt file into a temp folder
COPY requirements.txt /tmp/

# installing the requirements.txt file
RUN pip install -r /tmp/requirements.txt

# creating a non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# now time to actually add in the script!
COPY stargate.py .

# this is the command that will run when the container is started
CMD [ "python", "./stargate.py" ]
