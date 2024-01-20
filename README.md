# avito_parser
Simple parser for parsing ads from Avito.ru with Python(Selenium). 
Created with Selenium/undetected_chromedriver. Will be further developed for parsing images and etc.
In this case the ads was parsed based on the following filters:
1. City - Krasnodar;
2. Districts - Central, Zapadnyu, Prikubansky;
3. Price - up to 35,000 rubles
You can change them if you want to any other.


## Set up

Requires Python 3.5+ to work. Copy the project and install dependencies:

> pip install -r requirements.txt

You must also have the Google Chrome browser installed, any more or less recent version. The script was tested on version 120.

> python avito_parser.py

## Result of script

![изображение](https://github.com/IsaShakh/avito_parser/assets/57360844/98a6b482-8f70-41a9-9d48-0ca8a9162115)


