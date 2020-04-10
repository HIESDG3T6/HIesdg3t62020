cd ./patient_history
docker build -t g3t6/patient_history:1.0.0 .
docker run -p 5008:5008 -e dbURL=mysql+mysqlconnector://g3t6@host.docker.internal:3306/patient_history g3t6/patient_history:1.0.0