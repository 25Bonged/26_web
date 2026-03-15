import re

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    content = f.read()

# 1. Remove the "Made with Napkin" watermark text
content = re.sub(r'Made with\s*<svg.*?>.*?</svg>\s*Napkin', '', content, flags=re.IGNORECASE | re.DOTALL)
content = re.sub(r'>Made with.*?Napkin<', '><', content)

# Brute force search to delete the exact node containing "Made with Napkin"
# Found it in the SVG source earlier.
content = re.sub(r'<text[^>]*>Made with ⋈ Napkin</text>', '', content)

# 2. To fix the dark text, we can swap #2c2c2c to #818cf8 (a nice neon purple/indigo) in the SVG
content = content.replace('stroke="#2c2c2c"', 'stroke="#818cf8"')
content = content.replace('fill="#2c2c2c"', 'fill="#818cf8"')

# 3. Swap the SVG text fill from default to white
content = content.replace('fill="#f4f4f4"', 'fill="#ffffff"')

# 4. Try removing the specific node that contains the napkin watermark by coordinate roughly
# This is a bit hacky but it removes text labels containing the words
if "Napkin" in content:
    content = re.sub(r'<g[^>]*>\s*<text[^>]*>.*?Napkin.*?</text>\s*</g>', '', content, flags=re.DOTALL)

with open(html_path, "w") as f:
    f.write(content)
print("SVG text and strokes updated.")
