cd ./mailgun
docker build -t g3t6/mailgun:1.0.0 .
docker run -p 5000:5000 -e dbURL=mysql+mysqlconnector://g3t6@host.docker.internal:3306/mailgun g3t6/mailgun:1.0.0