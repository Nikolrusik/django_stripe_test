# How to run
This guide will help you to run this project

## Step 1
Make sure that you have Docker installed on your computer. You can download and install Docker from the [official website](https://www.docker.com/products/docker-desktop/).

## Step 2
To start, create a folder for project, open the terminal, and run the command
```
git clone https://github.com/Nikolrusik/django_stripe_test.git /yourfolder
```

## Step 3
Navigate to the project folder from the terminal and run the command:
```
docker-compose build app
```

If everything is successful, you will see something like this in the console:
```
Successfully built d41d802bfbf0
Successfully tagged stripe_app:latest
```

## Step 4
Now, run the command:
```
docker-compose up app
```
After running this command, the server with the database and the application should start, and you can then go to the link [https://localhost:8000/item/1](https://localhost:8000/item/1)

## Done!
