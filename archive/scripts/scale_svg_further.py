import re

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    content = f.read()

# Target the specific SVG line and force it to be massive using scale utilities
# Right now it has class "w-full max-w-[2000px] w-full mx-auto drop-shadow-2xl opacity-90 transition-all duration-700 hover:opacity-100"

new_svg_class = 'class="w-full max-w-none mx-auto drop-shadow-2xl opacity-90 hover:opacity-100 transform scale-[1.3] md:scale-[1.5] origin-top transition-transform duration-700"'

content = re.sub(r'class="w-full max-w-\[2000px\] w-full mx-auto drop-shadow-2xl opacity-90 transition-all duration-700 hover:opacity-100"', new_svg_class, content)

# Also ensure the container handles the overflow from scaling
# Right now it's <div class="glass-cyber rounded-3xl border border-white/5 p-2 md:p-6 lg:p-8 shadow-2xl shadow-neon-purple/10 flex justify-center w-full transform hover:scale-[1.01] transition-transform duration-500 bg-slate-900/50 backdrop-blur-xl">

content = content.replace('p-2 md:p-6 lg:p-8', 'p-8 md:p-24 pb-32 md:pb-56') # add padding back so the scaled SVG doesn't bleed out of the glass container

with open(html_path, "w") as f:
    f.write(content)

print("Scaled up SVG successfully.")
