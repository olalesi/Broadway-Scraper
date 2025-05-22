# 🎭 Broadway Show Scraper (Ticketmaster API)

This project is a Python-based scraper that uses Ticketmaster’s official Discovery API to fetch upcoming Broadway shows in New York. It saves data to CSV files with timestamps and logs each run for tracking and automation.

---

## ✅ Features

- Pulls live Broadway show data from Ticketmaster API
- Extracts:
  - Show Title
  - Show Date & Time
  - Venue and City
  - Ticket Link
  - Show Image URL
- Saves output to timestamped `.csv` files
- Appends each scrape to `scrape_log.txt`
- (Optional) Tracks seen shows for notifications via `seen_events.txt`
- Set up to run via Windows Task Scheduler

---

## 🚀 Setup Instructions

### 1. Install Python

Download Python from https://www.python.org/downloads/  
Make sure to check ✅ "Add Python to PATH" during installation.

---

### 2. Install Dependencies

Open your terminal or command prompt and run:
```bash
pip install requests
