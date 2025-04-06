import requests
from bs4 import BeautifulSoup
import re
import datetime

# URL of your film stats page
url = 'https://letterboxd.com/notstone/stats/'

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract stats
films_watched = soup.select_one('.stat-number:contains("Films")').text.strip()
hours = soup.select_one('.stat-number:contains("Hours")').text.strip()
directors = soup.select_one('.stat-number:contains("Directors")').text.strip()
countries = soup.select_one('.stat-number:contains("Countries")').text.strip()
longest_streak = soup.select_one('.stat-number:contains("Longest Streak")').text.strip()
multi_film_days = soup.select_one('.stat-number:contains("2+ Film Days")').text.strip()

# Extract top films (this would need to be adapted based on the actual HTML structure)
top_films = []
for film in soup.select('.top-films .film-card'):
    title = film.select_one('.film-title').text.strip()
    poster_url = film.select_one('img')['src']
    top_films.append({'title': title, 'poster_url': poster_url})

# Extract top directors
top_directors = []
for director in soup.select('.directors-list .director-item'):
    name = director.select_one('.director-name').text.strip()
    count = director.select_one('.director-count').text.strip()
    top_directors.append({'name': name, 'count': count})

# Update the HTML file
with open('film.html', 'r') as file:
    html = file.read()

# Update stats
html = re.sub(r'<div class="stat-number">\d+,?\d*</div>\s*<div class="stat-label">Films Watched</div>', 
              f'<div class="stat-number">{films_watched}</div>\n      <div class="stat-label">Films Watched</div>', html)
# Repeat for other stats...

# Update last updated date
today = datetime.datetime.now().strftime('%B %d, %Y')
html = re.sub(r'<span id="update-date">.*?</span>', f'<span id="update-date">{today}</span>', html)

# Write updated HTML
with open('film.html', 'w') as file:
    file.write(html)

print("Film stats updated successfully!")