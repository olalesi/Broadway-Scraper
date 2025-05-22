# 🎭 Broadway Show Scraper (Ticketmaster API)

This project is a Python-based scraper that uses Ticketmaster’s official Discovery API to fetch upcoming Broadway shows in New York. It saves data to CSV files with timestamps and logs each run for tracking and automation.

## ✅ Features

- Extracts show title, date, time, venue, city, image URL, and ticket link
- Saves results in timestamped CSV files
- Logs every run to `scrape_log.txt`
- Designed for use with Windows Task Scheduler

## 🚀 Setup Instructions

1. **Install Python**: [https://www.python.org/downloads](https://www.python.org/downloads)
2. **Install dependencies**:
```bash
pip install requests
```
3. **Edit `run_scraper.bat`**:
Update this line to match your folder location if needed:
```
cd "C:\Path\To\Your\Folder"
```

## ▶️ Manual Use
Run:
```bash
python broadway_scraper.py
```

## 🔁 Automate with Windows Task Scheduler
1. Open Task Scheduler
2. Create Basic Task
3. Trigger: Daily (e.g., 08:00 AM)
4. Action: Start a program → select `run_scraper.bat`

## 📄 Output Files
- `broadway_events_*.csv`: Show listings
- `scrape_log.txt`: Log of scrape runs

## 👤 Author
Built by Tobi as part of a web scraping technical assessment.
