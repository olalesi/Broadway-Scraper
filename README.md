🎭 Broadway Show Scraper (Ticketmaster API)
This project is a Python-based tool that scrapes upcoming Broadway shows in New York City using Ticketmaster’s official Discovery API. It automates the process of collecting event details, enhances the data with rich metadata, and saves the results neatly into CSV files for future use or analysis.

✅ Key Features
- Fetches show details: title, date, time, venue, type, ticket link, and image URL
- Uses Ticketmaster's API for accurate and enriched metadata
- Automatically saves results to timestamped CSV files
- Integrates Playwright automation to improve ticket link reliability
- Logs each scraping session to scrape_log.txt
- Ready for daily automation via Windows Task Scheduler

🛠️ Setup Guide
1. Install Dependencies
- Make sure Python is installed:
👉 [Download Python](https://www.python.org/downloads)
- Then, install the required libraries:
👉 pip install requests playwright
👉 playwright install
2. Configure Project Folder
Open broadway_scraper.py and set the PROJECT_FOLDER variable to your desired folder path. This is where your CSV files will be stored.

▶️ How to Use
Run the Scraper Manually
To run the scraper manually, use:
python broadway_scraper.py

🔁 Automate with Windows Task Scheduler
Want to automate the scraper to run daily? Follow these steps:
1. Open Task Scheduler on your Windows machine
2. Click Create Basic Task
3. Set a daily trigger (e.g., 8:00 AM)
4. Choose Start a program and point to run_scraper.bat
5. Save and you're done!
Your script will now run automatically each day.

📁 Output Files
- broadway_enriched_api_only_*.csv: Timestamped CSV with enriched event data
- scrape_log.txt: Log file for tracking each run and potential issues

👨‍💻 About the Project
Created by Olalesi for a technical web scraping assessment.
The project showcases a hybrid approach combining API usage with browser automation for reliable, structured, up-to-date Broadway show data.

