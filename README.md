# anime-downloader

This downloader was just a quick hack out of desperation but is up and working with a few hickups at the moment.
Any help with this project would be greatly appriciated!!

Ok so how does it work?

simple! Just install the requirements with:

pip3 install requirements.txt
(or just pip if you prefer)

download the geckodriver for firefox and export to your path

add your credetials to log in to gogoanime.vc to the script where labled

then run:
python3 selenium_scraper.py

This will initiate the script and once logged in you will be asked for the anime you would like to download 

IMPORTANT!!
This is still just a quick hacked together downloader.
For now it only works in the Firefox browser.
When entering the anime name ensure it is all lowercase and no special characters are added otherwise it will not work.
for example:
'To LOVE-Ru' would be 'to love ru'
Updates will come with an emproved parsing and search function as to minimize failures.

If you have any suggestions as to how I can emprocve this downloader or if you would like to add any funtionality please make a pull request and I would be more than happy to work with you!
