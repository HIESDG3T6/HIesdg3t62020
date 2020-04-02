cd ./insurance_claim
docker build -t g3t6/insurance_claim:1.0.0 .
docker run -p 5003:5003 -e dbURL=mysql+mysqlconnector://g3t6@host.docker.internal:3306/insurance_claim g3t6/insurance_claim:1.0.0