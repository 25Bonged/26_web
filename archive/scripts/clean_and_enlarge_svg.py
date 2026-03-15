import re

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    content = f.read()

# 1. Hide the Napkin logo by changing its fill to none or removing the path
# The Napkin logo is the last path in the SVG with fill="#ababab88"
content = content.replace('fill="#ababab88"', 'fill="none" display="none"')

# 2. Make the container much bigger
content = content.replace('max-w-[1400px]', 'max-w-[2000px] w-full')
content = content.replace('class="w-full max-w-[2000px] w-full mx-auto', 'class="w-full max-w-none mx-auto')

# 3. Reduce padding in the glass-cyber container so the image can take up more space
content = content.replace('p-4 md:p-12 shadow-2xl', 'p-2 md:p-6 lg:p-8 shadow-2xl')

with open(html_path, "w") as f:
    f.write(content)

print("Updated helix.html successfully to increase SVG size and remove watermark.")
