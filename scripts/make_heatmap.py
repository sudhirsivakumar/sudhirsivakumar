# scripts/make_heatmap.py
import requests
from bs4 import BeautifulSoup
import time

USERNAME = "sudhirsivakumar"
# The ?v= timestamp forces GitHub to bypass its cache and serve fresh data
url = f"https://github.com/users/{USERNAME}/contributions?v={int(time.time())}"

print(f"Fetching contributions for {USERNAME}...")
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

days = []
for td in soup.find_all("td", class_="ContributionCalendar-day"):
    level = td.get("data-level")
    if level is not None:
        days.append(int(level))

print(f"Found {len(days)} days of data. Drawing SVG...")

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
svg = '''<svg width="860" height="180" xmlns="http://www.w3.org/2000/svg">
    <style>
        .box { animation: slide-down 0.8s ease-out forwards; opacity: 0; }
        @keyframes slide-down {
            0% { transform: translateY(-10px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }
        text { font-family: 'Courier New', Courier, monospace; font-size: 14px; fill: #c9d1d9; font-weight: bold; }
    </style>
    <rect width="100%" height="100%" fill="#0d1117" rx="8" />
    <text x="30" y="30">sudhirsivakumar's Contributions</text>
    <g transform="translate(30, 50)">
'''

box_size = 11
gap = 4

for i, level in enumerate(days):
    col = i // 7
    row = i % 7
    x = col * (box_size + gap)
    y = row * (box_size + gap)
    color = PALETTE[min(level, 4)]
    delay = (col * 0.015) + (row * 0.015)
    svg += f'        <rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" fill="{color}" class="box" style="animation-delay: {delay}s;" />\n'

svg += """    </g>\n</svg>"""

with open("contrib-heatmap.svg", "w") as f:
    f.write(svg)
    
print("Successfully generated contrib-heatmap.svg!")