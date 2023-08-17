# This is the first image:
FROM ubuntu:20.04 AS compile-image
MAINTAINER HARIKRISHNA PALAKILA FROM INDIA
RUN apt-get update
RUN apt-get install -y python && apt-get update 
RUN mkdir /lmsapp

WORKDIR /lmsapp
COPY hello.py ./

# This is the second and final image; it copies the compiled
# binary over but starts from the base ubuntu:18.04 image.
FROM ubuntu:20.04 AS runtime-image

COPY --from=compile-image /lmsapp .
CMD [ "python", "./hello.py" ]