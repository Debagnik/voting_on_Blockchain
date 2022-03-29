Step 1: create the Docker image:

    docker build --tag vote-blocks:latest .


Step 2: create a container

    docker create --name prototype --tty --interactive vote-blocks:latest

Step 3: run the container

    docker start --attach --interactive prototype
