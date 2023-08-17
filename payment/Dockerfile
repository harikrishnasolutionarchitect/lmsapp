From ubuntu:20.04 as base-image
MAINTAINER harikrishna palakila
RUN apt-get update && apt-get install python
RUN mkdir /lmsapp
COPY emi-payment.py /lmsapp
ENTRYPOINT ["python"]
CMD ["/lmsapp/emi-payment.py"]