# This is the first image:
FROM ubuntu:18.04 AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc build-essential python

WORKDIR /usr/app/src/
COPY hello.py ./

# This is the second and final image; it copies the compiled
# binary over but starts from the base ubuntu:18.04 image.
FROM ubuntu:18.04 AS runtime-image

COPY --from=compile-image /usr/app/src .
CMD [ "python", "./hello.py" ]