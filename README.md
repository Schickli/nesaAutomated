# Nesa Automate

This project enables automatic execution of a script using a Docker container. 
## Prerequisites

In order to always receive the latest grades, the container must always be running. 
There are two ways to achieve this:
- Host the container online 
- Host it on your computer/Raspberry Pi.

Make sure the following components are installed on your system:
- Docker

## Configuration

Clone this repository to your computer.
Before running the script in a Docker container, you need to create a configuration file. Follow these steps:

- Create a file named .env in the project's root directory.
- Open the .env file and add the required environment variables. (Login_URL is the URL from your Nesa Site)$
- You can get the NOTI_URL from https://maker.ifttt.com/use/ and then click Documentation. You have to be logged in.
```
  USERNAME=user.name
  PASSWORD=yourpwd
  LOGIN_URL=https://gbs.nesa-sg.ch/loginto.php
  NOTI_URL=https://maker.ifttt.com/trigger/{nameOfYourTrigger}/with/key/{{YourKey}}
```
Ensure that you enter the correct values.

## Running the Script in a Docker Container

To execute the script in a Docker container, follow these steps:

- Navigate to the project's root directory where the Dockerfile is located.
- Open a terminal or command prompt and execute the following command to build the Docker image:
```
  docker build -t project-name .
```
Replace project-name with the desired name for the Docker image.

Once the Docker image is successfully built, run the following command to start the container:
```
docker run project-name
```
Again, replace project-name with the name of the Docker image.

The script will now execute within the Docker container. The necessary dependencies will be installed automatically, and the configuration data from the .env file will be used.

## Mobile Notification

To get notification on your mobile phone, we use IFTTT.
Go to https://ifttt.com and create an account. 
Now create a new applet with the trigger webhook and the action notification.

![grafik](https://github.com/Schickli/nesaAutomated/assets/67188361/3029d0b2-da96-4cc9-a3d6-17f9554fb84d)

![grafik](https://github.com/Schickli/nesaAutomated/assets/67188361/6c82be69-cac0-4f5b-9d9f-b76801fc6252)

![grafik](https://github.com/Schickli/nesaAutomated/assets/67188361/eaf429dc-4068-413e-b819-5564111ee133)

Don't forget to update the NOTI_URL with the name of the Webhook.
Now download the IFTTT App and your good to go!

## Additional Information

For any questions or issues, please raise an issue here on Github. 
