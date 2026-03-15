import re

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    content = f.read()

# 1. Match background color exactly. Change bg-slate-950 on the SVG section to bg-[#0B0E14] or transparent
# Section: <section class="pt-16 pb-0 bg-slate-950 flex justify-center w-full relative z-10 mb-12">
content = content.replace('bg-slate-950 flex justify-center w-full relative z-10 mb-12', 
                          'bg-[#0B0E14] flex justify-center w-full relative z-10 mb-24')

# 2. Match background color on the section below that to #0B0E14 as well, instead of slate-950
# Section: <section class="py-32 border-t border-slate-800 bg-slate-950" id="data">
content = content.replace('bg-slate-950" id="data"', 'bg-[#0B0E14]" id="data"')
# Also let's fix any bg-gradient-to-b from-transparent to-slate-950/50 pointer-events-none inside the SVG section
content = content.replace('to-slate-950/50', 'to-[#0B0E14]/50')

# 3. Mega zoom the SVG.
# w-full max-w-[1400px] mx-auto transform scale-110 md:scale-125 origin-top drop-shadow-2xl
content = content.replace('transform scale-110 md:scale-125 origin-top', 
                          'transform scale-125 md:scale-150 origin-top')

# We can also increase the viewBox a little bit just to make sure it trims perfectly
# Wait, no, we just scale it. 1.5x scale is huge. 

with open(html_path, "w") as f:
    f.write(content)

print("SVG MEGA Zoomed and bg color matched perfectly!")
