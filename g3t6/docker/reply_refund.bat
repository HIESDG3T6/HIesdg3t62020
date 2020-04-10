cd ./reply_refund
docker build -t g3t6/reply_refund:1.0.0 .
docker run -p 5001:5001 -e dbURL=mysql+mysqlconnector://g3t6@host.docker.internal:3306/insurance_claim g3t6/reply_refund:1.0.0