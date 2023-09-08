FROM python:3.10

WORKDIR /app
ADD /backend /app

RUN python -m pip install -r requirements.txt

EXPOSE 5000
ENV APP_PORT 5000

CMD [ "python", "main.py"]