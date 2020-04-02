cd ./pay
docker build -t g3t6/pay:1.0.0 .
docker run -p 3000:3000 -e dbURL=mysql+mysqlconnector://g3t6@host.docker.internal:3306/pay g3t6/pay:1.0.0