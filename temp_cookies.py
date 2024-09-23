import json

# Load the original cookie file
with open('cookies.json', 'r') as f:
    raw_cookies = json.load(f)

# Create a new dictionary with only the cookie name and value
cookies = {cookie['name']: cookie['value'] for cookie in raw_cookies}

# Save the new format back to the file
with open('cookies_cleaned.json', 'w') as f:
    json.dump(cookies, f)

print("Cookies have been cleaned and saved as cookies_cleaned.json")
