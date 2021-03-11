# General

Run a keywords-based search.  

Two scrapers are available:  
`webscraper.py` -> runs on requests library  
`seleniumscraper.py` -> runs on selenium library  
Choose one and launch the script as `python3 <chosen_scraper>.py`

The output is saved to csv and xlsl.  
Example of output for the keywords 'africa' and 'flowers':  

|    | title                                                                                                                                                                     |   publication_date | subject   | journal                                           | DOI                                                                                                                                      | author                              | abstract                                                                                                                                                                                                                                                                               | from_database   |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------:|:----------|:--------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
|  1 | Red flowers and butterfly pollination in the fynbos of South Africa                                                                                                       |               1994 |           | Plant-animal interactions in Mediterranean-type … | 10.1007/978-94-011-0908-6_13                                                                                                             | SD Johnson, WJ Bond                 | A guild of fynbos species with red flowers is pollinated exclusively by the butterfly Meneris tulbaghia. Such dependence on a single species of pollinator is rarely found in plants. Species pollinated by M. tulbaghia share several convergent characteristics including large …    | gs              |
|  2 | The Prosoeca peringueyi (Diptera: Nemestrinidae) pollination guild in southern Africa: long-tongued flies and their tubular flowers                                       |               1996 |           | Annals of the Missouri Botanical Garden           | https://www.jstor.org/stable/2399969                                                                                                     | JC Manning, P Goldblatt             | A guild of 28 winter-and spring-flowering species of two plant families, Iridaceae and Geraniaceae, with intense purple to crimson flowers and extremely long and slender perianth tubes, is pollinated exclusively by two long-tongued flies of the family …                          | gs              |
|  3 | Pollen wasps and flowers in southern Africa.                                                                                                                              |               2010 |           |                                                   | https://www.cabdirect.org/cabdirect/abstract/20113196209                                                                                 | SK Gess, FW Gess                    | This work is a treatment of pollen wasps as distinct from wasps in general and particularly of pollen wasps of southern Africa. The pollen wasps are behaviourally distinct from all other aculeate (stinging) wasps. Indeed in behaviour they are bee-like …                                                                                                                                                                                                                                                                                                                   | gs       

## INSTALLATIONS

### SELENIUM

`pip3 install selenium`

##### chromium for Chrome+Selenium

`sudo pacman -S chromium`

##### geckodriver for Firefox+Selenium [for reference, not necessary]
download https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz  
cd to the download directory  
then

```
tar -xvzf geckodriver-v0.29.0-linux64.tar.gz
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
```
