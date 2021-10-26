# Facebook Scrapper

A Facebook scrapping service using fastAPI and saving data in mongoDB

## Running the project

With docker compose : 

```bash
docker-compose up
```

or with docker (with mongo running )
```bash
docker build -t facebookscrapper .
docker run -d -p 8000:8000 -d facebookscrapper
```

## Usage
You can test the endpoints with swagger : 
![image description](https://i.imgur.com/O02sW9l.png)

![image description](https://i.imgur.com/QU7cYfw.png)

## Running tests
You can run tests with 
```bash
pytest
```
![image description](https://i.imgur.com/odJDYmB.jpeg)
