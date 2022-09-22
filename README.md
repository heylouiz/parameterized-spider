# parameterized-spider

A parameterized spider where you can configure the output stats for testing.

## Why?

Scrapy has a cool way to summarize the information about a spider run. It collects information during the run and
outputs them at the end, this feature is called stats.

See [Scrapy Stats documentation](https://docs.scrapy.org/en/latest/topics/stats.html)

These stats are a great source of information for a user or a program, where one can spot errors or inconsistencies without digging trough the logs.

This project has a spider that gives the user a way to modify some parts of the stats, this is useful when testing a external tool that consumes from job stats.

For example, if you have a script that checks for jobs that did not extract items but don't want to modify your spiders to make them fail, you could setup this project to be monitored and parameterize the spider to behave like it extracted 0 items.


## Setup and run

You can run this project on your machine using Python (preferably in a virtualenv) or Docker.

### Python

```
python -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
scrapy crawl parameterized
```

### Docker (compose)

```
docker-compose run scrapy scrapy crawl parameterized
```

## Supported parameters

The parameterization makes use of [Spider arguments](https://docs.scrapy.org/en/latest/topics/spiders.html#spider-arguments) to override Stats information.

Supported parameters, effects in Stats and usage.

### item_scraped_count

**Default value:**

`10`

**Effect in Stats**:
```
{
    'item_scraped_count': 20
}
```

**Usage:**

`scrapy crawl parameterized -a item_scraped_count=20`

### finish_reason

**Default value:**

`"finished"`

**Effect in Stats**:
```
{
    'finish_reason': 'custom reason'
}
```

**Usage:**

`scrapy crawl parameterized -a finish_reason="custom reason"`

### request_count

**Default value:**

`10`

**Effect in Stats**:
```
{
    'downloader/request_count': 100
}
```

**Usage:**

`scrapy crawl parameterized -a request_count=100`

### error_count

**Default value:**

`0`

**Effect in Stats**:
```
{
    'log_count/ERROR': 20,
}
```

**Usage:**

`scrapy crawl parameterized -a error_count=20`

### crawlera_banned

**Default value:**

`0`

**Effect in Stats**:
```
{
    'crawlera/response/banned': 10,
    'crawlera/response/error': 10,
    'crawlera/response/error/banned': 10
}
```

**Usage:**

`scrapy crawl parameterized -a crawlera_banned=10`

