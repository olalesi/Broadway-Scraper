import requests
import csv
from datetime import datetime

# --- CONFIGURATION ---
API_KEY = "GQWGVre90kF5LBNaGviEXl6AlyEouloY"
URL = f"https://app.ticketmaster.com/discovery/v2/events.json?classificationName=theatre&city=New%20York&countryCode=US&apikey={API_KEY}"

def run_scraper():
    print("⏰ Running Broadway show scraper...")

    # Step 1: Fetch data from API
    response = requests.get(URL)
    data = response.json()

    # Step 2: Extract show events
    events = data.get('_embedded', {}).get('events', [])
    print(f"✅ Found {len(events)} events.\n")

    # Step 3: Generate timestamped filename
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
    csv_file = f"broadway_events_{timestamp}.csv"

    # Step 4: Open CSV and write header
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Date", "Time", "Venue", "City", "URL", "Image URL"])

        for event in events:
            name = event.get('name')
            date = event.get('dates', {}).get('start', {}).get('localDate', 'N/A')
            time_ = event.get('dates', {}).get('start', {}).get('localTime', 'N/A')
            venue = event.get('_embedded', {}).get('venues', [{}])[0].get('name', 'N/A')
            city = event.get('_embedded', {}).get('venues', [{}])[0].get('city', {}).get('name', 'N/A')
            url = event.get('url', 'N/A')
            image_url = event.get('images', [{}])[0].get('url', 'N/A')

            # Print to terminal
            print(f"🎭 {name}\n📅 {date} ⏰ {time_}\n📍 {venue}, {city}\n🖼 {image_url}\n🔗 {url}\n" + "-" * 50)

            # Write to CSV
            writer.writerow([name, date, time_, venue, city, url, image_url])

    # Step 5: Log the run
    with open("scrape_log.txt", "a") as log:
        log.write(f"[{timestamp}] Scraped {len(events)} events -> {csv_file}\n")

    print(f"📁 Data saved to: {csv_file}")
    print(f"🗒️ Log updated in: scrape_log.txt\n")

# --- EXECUTE SCRAPER ---
if __name__ == "__main__":
    run_scraper()
