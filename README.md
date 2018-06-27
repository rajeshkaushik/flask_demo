# flask_demo
Sample flask project with docker and gunicorn


# Deploying with docker

## Build image

    docker build -t flask_demo:1 .

## Deploy image

    docker run -d -p 8000:8000 flask_demo:1