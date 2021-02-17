# install all python dependencies by using pipenv
# dev dependencies are included for testing purposes
install:
	cd backend; \
	pipenv install --dev

# run all backend tests
test:
	cd backend; \
	pipenv run python manage.py test

# build and set up and running containers
run:
	docker-compose up -d --build

# shutdown containers
stop:
	docker-compose down


all: install test run
