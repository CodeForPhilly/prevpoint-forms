
#copy docker image containing openCV
FROM jjanzic/docker-python3-opencv:opencv-4.0.0

COPY requirements.txt /

RUN pip install --no-cache-dir -r /requirements.txt
