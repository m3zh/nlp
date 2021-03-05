Two scrapers here:  

webscraper.py -> runs on requests library  
seleniumscraper.py -> runs on selenium library 

Choose one and launch the script as `python3 <chosen_scraper>.py`

# INSTALLATIONS

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
