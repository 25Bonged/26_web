import re

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    content = f.read()

# 1. Reduce the container padding.
# Old: p-8 md:p-24 pb-48 md:pb-80 pt-16 md:pt-32
# New: p-8 md:p-12 pb-32 md:pb-56 pt-8 md:pt-16
# Let's target the exact class string
old_padding = 'p-8 md:p-24 pb-48 md:pb-80 pt-16 md:pt-32'
new_padding = 'p-8 md:p-16 pb-24 md:pb-40 pt-4 md:pt-8'

content = content.replace(old_padding, new_padding)

# 2. Adjust the SVG viewBox to crop the top 30-40 pixels where the title used to be
# Old: viewBox="0 0 644 485"
# Also need to adjust height slightly since we are cropping.
# Let's crop top 40px: start Y at 40, height = 485 - 40 = 445
content = content.replace('viewBox="0 0 644 485"', 'viewBox="0 40 644 415"')

# Add -mt-8 to pull it up slightly inside the container
content = content.replace('origin-top"', 'origin-top -mt-4 md:-mt-8"')

with open(html_path, "w") as f:
    f.write(content)

print("Trimmed space successfully.")
