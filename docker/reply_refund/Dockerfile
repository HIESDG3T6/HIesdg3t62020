FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./reply_refund.py .
CMD [ "python", "./reply_refund.py" ]
