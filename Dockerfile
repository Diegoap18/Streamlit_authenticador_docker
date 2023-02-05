from ubuntu:20.04

WORKDIR /app
COPY . /app

RUN apt-get update && \
 apt-get install -y python3.9 && \
 apt-get install -y python3-pip && \
 apt-get install -y libgl1-mesa-glx
 
COPY requirements.txt requirements.txt
COPY db.pkl db.pkl

RUN pip3 install --upgrade setuptools && \
	pip3 install -r requirements.txt

EXPOSE 8501
	
CMD streamlit run app.py

















	
