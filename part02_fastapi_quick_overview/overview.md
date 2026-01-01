### Installation

In the fastapi documentations it is mentioned that we must install it using this command:
```
pip install "fastapi[standard]"
```
We must mention the double quotes to ensure that it runs on every terminal.

### How fastapi is different from flask?
Both fastapi and flask are web frameworks for python.

But the difference lies in their underlying architecture. Fastapi is built on ASGI(Asynchronous Gateway Interface) because of which it has native support for asynchronous code, can handle large number of requests concurrently. Because of it's non blocking request handling fastapi is pretty fast.

On the other hand, Flask is built on WSGI(Web Server Gateway Interface) because of which flask is synchronous in nature. It can't handle large number of requests concurrently, which makes flask comparatively slower.

Fastapi can handle 15000-20000 requests per seconds, whereas Flask can handle only 2000-5000 requests per second. Fastapi is built for high performance API development. And that is why fastapi is used for serving machine learning models, deep learning models, or LLMs as API.

We can also use python type hints along with pydantic to perform data validation in fastapi applications. Fastapi also provides swagger UI, where we can see and test the different routes, by providing them sample inputs. Flask do not have anything like that.

