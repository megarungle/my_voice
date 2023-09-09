# TODO: Add model.safetensors into docker image
FROM anibali/pytorch:2.0.1-nocuda-ubuntu22.04 

WORKDIR /app
ADD /backend /app

RUN python -m pip install -r requirements.txt

EXPOSE 5000
ENV APP_PORT 5000

CMD [ "python", "main.py"]
