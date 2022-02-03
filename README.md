# GenericAPI

Generic API using FastAPI. Mainly following the Udemy course [Complete Backend (API) Development with Python A-Z™](https://www.udemy.com/course/python-api-development/).

This repo is part of my portfolio and showcases my habilities in backend development. This API is big; might be good to have a smaller one for the portfolio.

The software I use to:
* VSCode for coding
* pgAdmin 4 as the database management tool
* Insomnia/Swagger to easily test the endpoints in development

So far I have used/done:

* Python types/typing/annotations
* Pydantic models
* Endpoints with adecuate labeling
* Testing the endpoints and requests with Insomnia
* Versioning (@ routes/)
* OAUTH 2.0 Authentication/Authorizations (@ utils/security.py)
    * Auth is required in /v2
* Middleware
* Switching fastapi.FastAPI with APIRouter
    * Allows calling dependencies (which helps with versioning and to add "differentiable middleware")
* Swagger documentation automatically generated
* Production Environment
    * Hosting in DigitalOcean
    * PostgreSQL
    * Docker
    * SQLAlchemy (I learned to use an ORM, but preferred to use pure SQL intead of this. SQL is simple enough.)
    * routing connections
    * PGAdmin 4 to easily access the database
    * SSH Authentication
* Connected the endpoints to a database
* Validation (just by using the correct sintax with `pydantic`, `typing`, `enum`, etc)
* Cache-ing with reddis
* Asyncronous tasks are handled with
    * asyncio (`await` command)
    * aioredis (is the lib to handle reddis)
* Endpoint testing
    * pytest in VSCode
* Load testing with Locust
* Deploying an API to production environment.
   * I hosted the servers (database+cache server and api server) as DigitalOcean Droplets.

Eventually, I might make an extremely verbose documentation to the code here contained, only to have a better understanding of everything if I see fit.
