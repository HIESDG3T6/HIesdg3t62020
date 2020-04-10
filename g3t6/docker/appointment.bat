cd ./appointment
docker build -t g3t6/appointment:1.0.0 .
docker run -p 4444:4444 -e dbURL=mysql+mysqlconnector://g3t6@host.docker.internal:3306/appointment g3t6/appointment:1.0.0