From ubuntu:20.04 as base-image
MAINTAINER harikrishna palakila
RUN apt-get update
RUN apt-get install -y python && apt-get update 
RUN mkdir /lmsapp
COPY emi-payment.py /lmsapp
ENTRYPOINT ["python"]
CMD ["/lmsapp/emi-payment.py"]