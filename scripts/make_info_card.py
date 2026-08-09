details = [
    ("Title", "B.E. Computer Science @ Bannari Amman Institute of Technology"),
    ("Stack", "Full-stack development, Go , Node.js, Flutter, MYsql, React/Angular, HTML, VanilaCSS, Tailwind CSS, Android Development"),
    ("Highlight", "AI augmented developer, Tech Enthusiast and a passionate learner."),
]

svg_content = """<svg width="490" height="250" xmlns="http://www.w3.org/2000/svg">
    <style>
        .text { font-family: 'Courier New', Courier, monospace; font-size: 14px; fill: #c9d1d9; opacity: 0; animation: fade-in 0.5s forwards; }
        .key { fill: #79c0ff; font-weight: bold; }
        .title { fill: #58a6ff; font-weight: bold; font-size: 16px; opacity: 0; animation: fade-in 0.5s forwards; }
        @keyframes fade-in {
            to { opacity: 1; }
        }
    </style>
    <rect width="100%" height="100%" fill="#0d1117" rx="8" />
    
    <text x="20" y="40" class="title" style="animation-delay: 0.1s;">sudhirsivakumar@github</text>
    <text x="20" y="55" class="text" style="animation-delay: 0.2s;">----------------------</text>
"""

y_pos = 85
delay = 0.3

for key, value in details:
    svg_content += f"""
    <text x="20" y="{y_pos}" class="text" style="animation-delay: {delay}s;">
        <tspan class="key">{key.ljust(10)} :</tspan> {value}
    </text>"""
    y_pos += 30
    delay += 0.2

svg_content += "\n</svg>"

with open("info-card.svg", "w") as f:
    f.write(svg_content)
    
print("Successfully generated info-card.svg!")