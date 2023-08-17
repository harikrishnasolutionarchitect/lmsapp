From ubuntu:20.04 as base-image
MAINTAINER harikrishna palakila from LMS Finance Management Pvt. Ltd
RUN apt-get update
RUN apt-get install -y python && apt-get update 
RUN mkdir /lmsapp
COPY emi-payment.py /lmsapp
ENTRYPOINT ["python"]
CMD ["/lmsapp/emi-payment.py"]

From ubuntu:20.04 as final-image
COPY --from=base-image /lmsapp/emi-payment.py ./
ADD car-emi-payment.py ./
ENTRYPOINT ["python"]
CMD ["/lmsapp/car-emi-payment.py"]
EXPOSE 80


From ubuntu:20.04 as final-2-image
COPY --from=final-image ./ ./
ADD car-emi-payment.py Total_emi_Adding_EMi_Amount.py ./
ENTRYPOINT ["python"]
CMD ["/lmsapp/Total_emi_Adding_EMi_Amount.py"]
EXPOSE 80

FROM nginx:stable-alpine AS ngi
COPY --from=final-2-image ./ /usr/share/nginx/html
ADD nginx.conf /etc/nginx/conf.d/lmsap-nginx.conf
EXPOSE 80




