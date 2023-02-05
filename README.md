# Streamlit_authenticador_docker
This repository is to share a simple Streamlit authenticador app on docker ubuntu 20.04\

<br >
#Instructions:\
this app run well on python 3.9 or later.\
you need a docker later version installed.\

#ON DOCKER FILE:\
You have the steps to install dependencies and features to ubuntu.\

to run you can open a Terminal CMD and run the following commands:\

#COMMAND:
docker build -f Dockerfile -t appteste:latest .\
docker run -it -p 8501:8501 appteste \
