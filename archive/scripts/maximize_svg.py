import re

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    content = f.read()

# 1. Remove the "HELIX Variant Control Workflow" text element
# Found in the SVG as:
# <g id="g-root-tx_helixvar_4pfn61uvljb4-fill" data-item-order="1000000000" transform="translate(167.21875, 3)"><g id="tx_helixvar_4pfn61uvljb4-fill-merged" stroke="none" fill="#f4f4f4" fill-opacity="1"><g><text ...>HELIX Variant Control Workflow</text></g></g></g>
content = re.sub(r'<g id="g-root-tx_helixvar.*?</g></g></g>', '', content, flags=re.DOTALL)
content = re.sub(r'<g id="g-root-tx_helixvar_4pfn61uvljb4-stroke".*?</g>', '', content, flags=re.DOTALL)

# Also let's just make absolutely sure by doing a pure string replace if the regex missed anything nested weirdly
if "HELIX Variant Control Workflow" in content:
        # Since it's inside the <svg> block, removing just the title <text> block is safest.
        content = re.sub(r'<text[^>]*>.*?HELIX Variant Control Workflow.*?</text>', '', content, flags=re.DOTALL)

# 2. Make it even more zoomed
# Current class contains: scale-[1.3] md:scale-[1.5]
content = content.replace('scale-[1.3] md:scale-[1.5]', 'scale-[1.5] md:scale-[1.8]')

# 3. Increase padding to compensate for larger scale so it doesn't clip
content = content.replace('p-8 md:p-24 pb-32 md:pb-56', 'p-8 md:p-24 pb-48 md:pb-80 pt-16 md:pt-32')


with open(html_path, "w") as f:
    f.write(content)

print("Title removed and zoom increased successfully.")
