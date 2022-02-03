# Webscraping : Automatic Web Scrapper using Python

![image](https://user-images.githubusercontent.com/69267132/152418573-1ff1e798-724a-4fbc-82fd-b670263ade29.png)

I wrote this code for automatic a web tv show page. The purpose of the project was to able to get a url content of a web page and list of sample date that we want to scrape.

## Installation

- Open project folder using Anaconda Prompt

```bash
$ cd
```

- Create a directory 
 
 ```bash
$ mkdir directory
```
- Create a virtual environment
 ```bash
$ conda create -n directory python=3.6
```
 ```bash
$ Proceed ([y]/n)? y
```
In Web Documentation Scrapy it is suggest to do this step

- Activate virtual environment 

 ```bash
$ conda activate directory
```
- Install from PyPI:
```bash
$ pip install scrapy
```

## How to use

Create a project using a text editor

- Open the text editor prompt or continue in Anaconda Prompt
```bash
$ scrapy startproject (insert a name)
```
- Start your first spider
```bash
$ cd (project name)
```
```bash
$ scrapy genspider (project name)
```
This last command creat a archive. Now we can say want we want.

```python
import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'projectName'
    start_urls = ['https://www.imdb.com/list/ls095964455/']

    def parse(self, response):
        for series in response.css('.mode-detail'):
            yield{
                'titulo': series.css('.lister-item-header a::text').get(),
                'ano': response.css('.text-muted.unbold ::text').get(),
                'nota': response.css('.ipl-rating-star.small .ipl-rating-star__rating ::text').get()
            }
```
Easy, right?

### Saving the model

We can save the built model to use it later. To save:

 ```bash
$ scrapy crawl (project name) -O (project name).json
```
