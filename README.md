# floor search
Price checking website tool for floor materials and elements, with the use of scrapy spiders/crawlers. 
Extracting product data to dump into Django models database

Inspired by tutorial:
https://medium.com/@ali_oguzhan/how-to-use-scrapy-with-django-application-c16fabd0e62e

using simple jQuerry ajax, instead of React component from the tutorial

to run a bot and observe it's work:
1. Add DATABASES setting, with creation of local_settings.py (safety first :) )
2. Start Django runserver command from floor_search/ directory
3. Start scrapyd-api by running "scrapyd" in the floor_search/crawler directory to look at the job running

Some of the settings in the files have additional comments, will add more in future, as well as a TODO list, 
since project is far from being finished
