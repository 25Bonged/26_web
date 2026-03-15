import re

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    content = f.read()

# 1. Match background color exactly with the Hero (#050508)
content = content.replace('bg-[#0B0E14] flex justify-center w-full relative z-10 mb-24', 
                          'bg-[#050508] flex justify-center w-full relative z-10 mb-24')

content = content.replace('bg-gradient-to-b from-transparent to-[#0B0E14]/50 pointer-events-none', 
                          'bg-gradient-to-b from-transparent to-[#050508]/50 pointer-events-none')

content = content.replace('bg-[#0B0E14]" id="data"', 'bg-[#050508]" id="data"')
# Also fix collaboration section to match!
content = content.replace('bg-slate-950" id="collaboration"', 'bg-[#050508]" id="collaboration"')
content = content.replace('h-48 bg-slate-950 rounded', 'h-48 bg-[#050508] rounded')

with open(html_path, "w") as f:
    f.write(content)

print("SVG and Backgrounds perfectly synced!")
