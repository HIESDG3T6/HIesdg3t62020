cd ./patient
docker build -t g3t6/patient:1.0.0 .
docker run -p 5555:5555 -e dbURL=mysql+mysqlconnector://g3t6@host.docker.internal:3306/patient g3t6/patient:1.0.0