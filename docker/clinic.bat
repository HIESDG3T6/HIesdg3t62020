cd ./clinic
docker build -t g3t6/clinic:1.0.0 .
docker run -p 5111:5111 -e dbURL=mysql+mysqlconnector://g3t6@host.docker.internal:3306/clinic g3t6/clinic:1.0.0