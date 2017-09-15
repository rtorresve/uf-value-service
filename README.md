# Technical test microservice to get the UF Values

## RESUME

The target about this project consist to get the historical information about the value of UF from the web Central Bank of Chile web page.

## Technical descriptions


I used a lot of plugins and elements in this project one of most important was the [JSONAPI](http://jsonapi.org/) implementation becuase I like this to maintain some standard, in other hand I use flake8 to maintain all the code, and added some pytest scripts, in other hand I use selenium and beautifulsoup package to get the data and finally I used phantomJS like my WebDriver, however I tried unsuccessfully to implement a dockerized enviroment, the main issue was because the selenium script was to slow to get the data when i used some reote web drivers and was to complicate for me find or create one image to upload the celery services with a most recent version of phantomjs.

## Endpoints


```[ GET: /v1/indicators/uf/ ]``` This is the main endpoint, and we use this to get al hystorical information about UF. and this request finnaly response a data with this pattern:

```
{
    "links": {
        "first": "http://devtest.bid/v1/indicators/uf/?page=1",
        "last": "http://devtest.bid/v1/indicators/uf/?page=734",
        "next": "http://devtest.bid/v1/indicators/uf/?page=2",
        "prev": null
    },
    "data": [
        {
            "type": "uf",
            "id": "14528",
            "attributes": {
                "date": "1977-08-01",
                "value": "389.10"
            }
        },
        {
            "type": "uf",
            "id": "14529",
            "attributes": {
                "date": "1977-08-02",
                "value": "389.51"
            }
        },
        :
        :
        :
     ],
    "meta": {
        "pagination": {
            "page": 1,
            "pages": 734,
            "count": 14680
        }
    }
}
```




```[ GET: /v1/indicators/uf/?date=2015-05-19&value=2345.67 ]``` We can filter the UF by data or/and value and It response is like



```
{
    "links": {
        "first": "http://devtest.bid/v1/indicators/uf/?date=2017-09-01&page=1",
        "last": "http://devtest.bid/v1/indicators/uf/?date=2017-09-01&page=1",
        "next": null,
        "prev": null
    },
    "data": [
        {
            "type": "uf",
            "id": "244",
            "attributes": {
                "date": "2017-09-01",
                "value": "26605.81"
            }
        }
    ],
    "meta": {
        "pagination": {
            "page": 1,
            "pages": 1,
            "count": 1
        }
    }
}
```

## The scrapper


To get all the historical data I created a manage comand that invoke to other asynchronous function you can see this command when you type the sentence

```python manage.py -h```

And to use this you need pass two integers to get the historical information between both.

```python manage.py get_hystoric_uf_value_by_year -f 2001 -t 2016```



## DEPLOY

Is very important that you set your custom setting in a json file in `api/` path with the name <strong>config.json</strong> you can use the config.json.example

Finally you can deploy this projec with the 

```python manage.py runserver``` 

and to deploy the worker use

```celery -A apps.tasks.celery worker -l INFO```

and if you do not use a external borker services you need run

``` celery -A project_name.taskapp beat -l INFO```

In my particular case I generally use [CloudAMQP](https://cloudamqp.com/) to tryed my personal projects


<u>Import!!!</u> please add the absolute path to you custom <b>conf.json</> in the manage.py and apps.tasks.celery.py files


## The Demo

To show a live demo use any REST client to endpoints in the domain (http://devtest.bid)[http://devtest.bid]





