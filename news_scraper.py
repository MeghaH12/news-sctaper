import requests
from bs4 import BeautifulSoup

# Target URL for CNN
url = "https://www.cnn.com"
headers = {"User-Agent": "Mozilla/5.0"}

# Fetch HTML content
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract headlines (this part is site-specific and might need adjustment for other websites)
# For CNN, headlines are often found within <h2> or <h3> tags with specific classes or attributes.
# We'll try to find elements that look like headlines. This might require inspection of the page source.
# Let's try a common pattern for headline links.
headlines = soup.find_all(["h2", "h3"])

# Extract and clean the text from the headline tags
# Filter out empty strings and potentially non-headline content
top_headlines = [tag.get_text(strip=True) for tag in headlines if tag.get_text(strip=True)]

# Print the first 10 extracted headlines in the requested format
print("CNN Headlines:")
for i, title in enumerate(top_headlines[:10], start=1):
    print(f"{i}. {title}")
