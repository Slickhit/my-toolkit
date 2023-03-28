import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import PySimpleGUI as sg


def get_links(url):
    # Send a GET request to the URL and parse the HTML response
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <a> tags and extract the href attribute
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    
    # Convert relative links to absolute links
    base_url = urlparse(url).scheme + '://' + urlparse(url).netloc
    links = [urljoin(base_url, link) for link in links]
    
    return links


def generate_sitemap(url):
    # Create a new sitemap object
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Add the homepage URL to the sitemap
    sitemap += f'    <url>\n        <loc>{url}</loc>\n    </url>\n'
    
    # Get all links from the website
    links = get_links(url)
    
    # Add each link to the sitemap
    for link in links:
        sitemap += f'    <url>\n        <loc>{link}</loc>\n    </url>\n'
    
    # Close the sitemap XML tag
    sitemap += '</urlset>'
    
    return sitemap


# Create the GUI window
layout = [
    [sg.Text('Enter website URL: '), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('Sitemap Generator', layout)

# Run the GUI loop
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    elif event == 'Submit':
        # Generate the sitemap for the entered URL
        url = values[0]
        sitemap = generate_sitemap(url)
        
        # Write the sitemap to a file
        with open('sitemap.xml', 'w') as f:
            f.write(sitemap)
        
        # Show a success message
        sg.popup('Sitemap generated successfully!')
        
# Close the GUI window
window.close()
