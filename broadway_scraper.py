import asyncio
import time
import csv
import os
import requests
from playwright.async_api import async_playwright

# Configuration
API_KEY = "GQWGVre90kF5LBNaGviEXl6AlyEouloY"
API_URL = "https://app.ticketmaster.com/discovery/v2/events.json"
PROJECT_FOLDER = "C:/Users/SAIL/Desktop/My Personal"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def query_ticketmaster_api(title):
    params = {
        "apikey": API_KEY,
        "keyword": title,
        "size": 1,
    }

    try:
        response = requests.get(API_URL, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        events = data.get("_embedded", {}).get("events", [])
        if not events:
            return None

        event = events[0]
        return {
            "title": event.get("name", "N/A"),
            "date": event.get("dates", {}).get("start", {}).get("localDate", "N/A"),
            "time": event.get("dates", {}).get("start", {}).get("localTime", "N/A"),
            "venue": event.get("_embedded", {}).get("venues", [{}])[0].get("name", "N/A"),
            "type": event.get("classifications", [{}])[0].get("segment", {}).get("name", "N/A"),
            "image": event.get("images", [{}])[0].get("url", "N/A"),
            "link": event.get("url", "N/A")
        }
    except Exception as e:
        print(f"⚠️ API error for '{title}': {e}")
        return None

async def scrape_broadway():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print("🌐 Visiting Broadway page...")
        await page.goto("https://www.ticketmaster.com/broadway", timeout=90000)
        await page.wait_for_selector("a:has-text('Find Tickets')", timeout=90000)

        print("🔄 Scrolling to load more shows...")
        for _ in range(10):
            await page.mouse.wheel(0, 1000)
            time.sleep(1)

        print("🔍 Extracting show links and titles...")
        links = await page.query_selector_all("a:has-text('Find Tickets')")
        print(f"✅ Found {len(links)} ticket links\n")

        results = []
        seen_titles = set()

        for link in links:
            try:
                href = await link.get_attribute("href")
                if not href:
                    continue

                full_url = "https://www.ticketmaster.com" + href if not href.startswith("http") else href

                # Attempt to extract title
                title = await link.evaluate("""
                    (node) => {
                        let parent = node.closest('div')?.parentElement;
                        if (!parent) return "Unknown Title";
                        let tags = parent.querySelectorAll('span, h3, h2, strong');
                        for (let el of tags) {
                            let text = el.innerText?.trim();
                            if (text && !/find tickets/i.test(text) && text.length > 4) return text;
                        }
                        return "Unknown Title";
                    }
                """)

                if title in seen_titles or "Find Tickets" in title or len(title.strip()) < 4:
                    continue

                seen_titles.add(title)
                print(f"🎭 {title} - looking up metadata...")

                data = query_ticketmaster_api(title)
                if not data:
                    print(f"⛔ No API match for: {title}")
                    continue

                results.append(data)
                print(f"📍 {data['venue']} | {data['date']} {data['time']}\n🖼 {data['image']}\n🔗 {data['link']}\n{'-'*50}")

            except Exception as e:
                print(f"⚠️ Skipped one due to error: {e}")

        # Save results to CSV
        timestamp = time.strftime("%Y-%m-%d_%H-%M")
        filename = f"broadway_scraper_{timestamp}.csv"
        filepath = os.path.join(PROJECT_FOLDER, filename)

        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "date", "time", "venue", "type", "image", "link"])
            writer.writeheader()
            writer.writerows(results)

        print(f"\n📁 Done. Saved {len(results)} shows to: {filepath}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_broadway())
