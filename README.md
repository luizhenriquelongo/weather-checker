# Weather Buddy :sun_behind_small_cloud:

Hello there! This project was very fun to develop and it's a cool weather buddy that can help you to know the weather on a specific city... let me show you how to try it.
## The Options

- If you just want to try it out, you can [click here](https://ec2-18-230-74-213.sa-east-1.compute.amazonaws.com/) and have some fun!
- If you want to set it up and running on your own machine, you can follow the tutorial bellow.

## Installation

>#### Requirements:
>- [Docker](https://docs.docker.com/get-docker/)
>- [Docker Compose](https://docs.docker.com/compose/install/)
>- [Make](https://www.gnu.org/software/make/manual/make.html)*

### 1. The .env file
The application needs some environment variables to run properly, you can copy the `.env.example` and config your own vars.
At *{project root}*/backend you can call the command:
```bash
$ cp .env.example .env
```
Use the comments on `.env.example` to help you edit the `.env` file.

### 2. Running the Project

At the project root directory, you should use the command:

```bash
$ make run
```
When the command finished its execution, you should be good to go and be able to access the application at `http://localhost/`
## Tests
>#### Requirements:
>- [Python 3.8](https://www.python.org/downloads/)
>- [Pip](https://pip.pypa.io/en/stable/installing/)
>- [Pipenv](https://pypi.org/project/pipenv/)
>- [Make](https://www.gnu.org/software/make/manual/make.html)*

To run the tests use the following commands:

```bash
$ make install && make tests
```
## To do:

- Frontend tests using jest;
- Do some cool stuff in the frontend using CSS;

## Author

- [Luiz Henrique Longo](https://linkedin.com/in/luizhenriquelongo)
>**Make is used in gnu based system, if it's not your case, you can open the `Makefile` and execute the same commands used on the script you're trying to run.*
