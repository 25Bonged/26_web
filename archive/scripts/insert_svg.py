import sys

with open("pics/helix.svg", "r") as f:
    svg_content = f.read()

# Add standard tailwind classes for sizing and centering
svg_styled = svg_content.replace('<svg ', '<svg class="w-full max-w-4xl mx-auto drop-shadow-2xl" ')

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    html_content = f.read()

# The target area is just before the Data Pipeline section
target = '<!-- Data Pipeline Section -->'
replacement = f"""
    <!-- Visual Separation / SVG Flow -->
    <section class="py-16 bg-slate-950 flex justify-center w-full relative z-10 -mb-16">
        <div class="absolute inset-0 bg-gradient-to-b from-transparent to-slate-950/50 pointer-events-none"></div>
        {{{{SVG}}}}
    </section>

    {target}
"""
replacement = replacement.replace('{{SVG}}', svg_styled)

if target in html_content:
    new_html = html_content.replace(target, replacement)
    with open(html_path, "w") as f:
        f.write(new_html)
    print("SVG inserted successfully.")
else:
    print("Could not find target section in HTML.")
