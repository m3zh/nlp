# General

Run a keywords-based search.
Example of output:

'''
title publication_date subject                   journal                       DOI                    author                  abstract from_database
0  Field guide to wild f...             2013                                    https://books.google....                 J Manning  Field Guide to Wildfl...            gs
1  Red flowers and butte...             1994          Plant-animal interact...  10.1007/978-94-011-09...       SD Johnson, WJ Bond  A guild of fynbos spe...            gs
2  The Prosoeca peringue...             1996          Annals of the Missour...  https://www.jstor.org...   JC Manning, P Goldblatt  A guild of 28 winter-...            gs
3  Pollen wasps and flow...             2010                                    https://www.cabdirect...          SK Gess, FW Gess  This work is a treatm...            gs
4    The culture of flowers             1993                                    https://books.google....                   J Goody  … He begins his study...            gs
5  Ornithophilous flower...             1890                  Annals of Botany  https://www.jstor.org...           GF Scott-Elliot  Melianthus Major, L.(...            gs
6  … Moegistorhynchus lo...             1997          Plant Systematics and...        10.1007/BF00987941   JC Manning, P Goldblatt  A guild of 20 late sp...            gs
7  Chemical composition ...             2009                         Molecules  https://www.mdpi.com/...  LA Oladipupo, OO Adebola  The essential oils of...            gs
8       Not without flowers             2007                                    https://muse.jhu.edu/...                   A Darko  … Not Without Flowers...            gs
9  A thousand flowers: S...             2000                                    https://books.google....  S Federici, CG Caffen...  Combining theoretical...            gs
'''
#### Scrapers

Two scrapers available:  

webscraper.py -> runs on requests library  
seleniumscraper.py -> runs on selenium library

Choose one and launch the script as `python3 <chosen_scraper>.py`

#### INSTALLATIONS

[SELENIUM]

`pip3 install selenium`

### chromium for Chrome+Selenium

`sudo pacman -S chromium`

### geckodriver for Firefox+Selenium
[download] https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz  
[cd] to the download directory  
then

```
tar -xvzf geckodriver-v0.29.0-linux64.tar.gz
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
```
