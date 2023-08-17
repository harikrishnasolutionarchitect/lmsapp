#!/bin/bash

#docker build -t emi-payment-image .
docker run -name emi-payment-container-01 emi-payment-image:latest

#docker build -t car-emi-payment-image .
docker run -name car-emi-container-02 car-emi-payment-image:latest /lmsapp/car-emi-payment.py