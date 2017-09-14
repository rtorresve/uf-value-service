FROM rafasis1986/python-mysql:3.6

RUN apk add --update build-base py-greenlet
 
RUN addgroup -S django \
    && adduser -S -g django django

COPY ./api/requirements/ /requirements

COPY ./compose/production/django/gunicorn.sh /gunicorn.sh

COPY ./compose/production/django/celery/worker/start.sh /celeryworker.sh

COPY ./api /app

RUN pip3 install --no-cache-dir -r /requirements/production.txt \
    && sed -i 's/\r//' /gunicorn.sh \
    && chmod +X /gunicorn.sh \
    && sed -i 's/\r//' /celeryworker.sh \
    && chmod +X /celeryworker.sh

WORKDIR /app

RUN chown -R django:django /app

USER django

WORKDIR /app
