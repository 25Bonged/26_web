import re

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    content = f.read()

# 1. Zoom the SVG more. Replace max-w-4xl with max-w-6xl
content = content.replace('max-w-4xl mx-auto', 'max-w-6xl mx-auto')

# 2. Crop the bottom section. Drop down the viewBox height manually to chop off the bottom watermark area
# The viewBox is currently "0 0 644 485". We'll snip off the bottom ~50 pixels.
content = content.replace('viewBox="0 0 644 485"', 'viewBox="0 0 644 430"')

# Also reduce the padding on the section itself: "py-16 ... -mb-16" -> "pt-16 pb-4 ... -mb-8"
content = content.replace('<section class="py-16 bg-slate-950 flex justify-center w-full relative z-10 -mb-16">',
                          '<section class="pt-16 pb-0 bg-slate-950 flex justify-center w-full relative z-10 -mb-8">')

# 3. Completely obliterate the "Made with Napkin" logo by finding its exact drawing path cluster at the end.
# It ends with path id "w18lbgahrjf5zh". We'll just remove that path entirely.
content = re.sub(r'<path id="w18lbgahrjf5zh".*?></path>', '', content)

with open(html_path, "w") as f:
    f.write(content)

print("SVG fixed!")
