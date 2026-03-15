import re

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    content = f.read()

content = content.replace("scale-[1.5] md:scale-[1.8]", "scale-[1.35] md:scale-[1.6]")

with open(html_path, "w") as f:
    f.write(content)

print("SVG scaled down by ~10%")
