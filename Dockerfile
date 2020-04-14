FROM python:3.8-alpine

WORKDIR /devetek

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]
