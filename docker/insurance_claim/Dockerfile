FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./insurance_claim.py .
CMD [ "python", "./insurance_claim.py" ]
