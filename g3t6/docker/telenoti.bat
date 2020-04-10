cd ./teleNoti
docker build -t g3t6/telenoti:1.0.0 .
docker run -p 4646:4646 -e dbURL=mysql+mysqlconnector://g3t6@host.docker.internal:3306/notification g3t6/telenoti:1.0.0