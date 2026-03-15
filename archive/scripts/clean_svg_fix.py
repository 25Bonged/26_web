import re

with open("pics/helix.svg", "r") as f:
    svg_content = f.read()

# 1. Hide the Napkin logo
svg_content = svg_content.replace('fill="#ababab88"', 'fill="none" display="none"')

# 2. Make SVG scalable and huge
svg_content = svg_content.replace('<svg ', '<svg class="w-full max-w-none mx-auto drop-shadow-2xl opacity-90 transition-all duration-700 hover:opacity-100 transform scale-[1.5] md:scale-[1.8] origin-top" ')

# 3. Remove the exact title string ONLY, leave structure intact
svg_content = svg_content.replace('HELIX Variant Control Workflow', '')

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    html_content = f.read()

# Instead of complex regex replacing previous broken SVG, 
# let's just grab the whole container block and replace it with a fresh one
new_section = f"""
    <!-- Visually stunning Workflow Section -->
    <section class="py-24 border-t border-slate-800 relative bg-[#030305] overflow-hidden">
        <!-- Background Accents -->
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-4xl h-px bg-gradient-to-r from-transparent via-neon-purple/50 to-transparent"></div>
        <div class="absolute -top-32 left-1/2 -translate-x-1/2 w-[800px] h-[300px] bg-neon-purple/5 blur-[120px] rounded-full point-events-none"></div>
        
        <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center mb-16">
                <h2 class="text-neon-purple font-bold tracking-widest uppercase text-sm mb-4 animate-pulse">Enterprise Variant Control</h2>
                <h3 class="text-3xl md:text-5xl font-bold text-white mb-6">Automated Workflow & Immutable Releases</h3>
                <p class="text-slate-400 max-w-3xl mx-auto text-lg">
                    A completely tracked pipeline from the moment a project root is initialized to the final, immutable production freeze. Zero data loss. Complete auditability.
                </p>
            </div>
            
            <div class="glass-cyber rounded-3xl border border-white/5 p-8 md:p-24 pb-48 md:pb-80 pt-16 md:pt-32 shadow-2xl shadow-neon-purple/10 flex justify-center w-full transform hover:scale-[1.01] transition-transform duration-500 bg-slate-900/50 backdrop-blur-xl">
                {svg_content}
            </div>
        </div>
    </section>"""

# Replace the entire section via regex
pattern = r'<!-- Visually stunning Workflow Section -->.*?</section>'
result = re.sub(pattern, new_section, html_content, flags=re.DOTALL)

with open(html_path, "w") as f:
    f.write(result)

print("SVG restored and text removed cleanly without breaking nodes.")
