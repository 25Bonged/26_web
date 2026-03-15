import re

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    content = f.read()

# Increase max-width and use scale for extra zoom
content = content.replace('w-full max-w-6xl mx-auto', 'w-full max-w-[1400px] mx-auto transform scale-110 md:scale-125 origin-top')

# Increase bottom margin slightly to account for the scale so it doesn't bleed into the next section
content = content.replace('z-10 -mb-8', 'z-10 mb-12')

with open(html_path, "w") as f:
    f.write(content)

print("SVG zoomed again!")
