cd ./notification
docker build -t g3t6/notification:1.0.0 .
docker run -p 5566:5566 -e dbURL=mysql+mysqlconnector://g3t6@host.docker.internal:3306/notification g3t6/notification:1.0.0