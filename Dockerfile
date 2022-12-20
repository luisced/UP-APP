FROM python:3.10.7-buster
WORKDIR /school_manager
COPY . .
ENV LANG es_MX.UTF-8 
ENV LC_ALL es_MX.UTF-8
ENV TZ=America/Mexico_City
ENV FLASK_ENV development
ENV DEBUG true
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install --upgrade pip && pip3 install -r requirements.txt
CMD ["python", "App/run.py"]
EXPOSE 5555