# Streamlit_authenticador_docker
This repository is to share a simple Streamlit authenticador app on docker ubuntu 20.04 <br >


# Instructions: <br >
this app run well on python 3.9 or later.<br >
you need a docker later version installed.<br >

# On DockerFile: <br >
You have the steps to install dependencies and features to ubuntu.<br >
to run you can open a Terminal CMD and run the following commands:<br >

# Commands:
docker build -f Dockerfile -t appteste:latest .<br >
docker run -it -p 8501:8501 appteste
