import re

# Read SVG
with open("pics/helix.svg", "r") as f:
    svg_content = f.read()

# Make SVG responsive and styled
svg_styled = svg_content.replace('<svg ', '<svg class="w-full max-w-[1400px] mx-auto drop-shadow-2xl opacity-90 transition-all duration-700 hover:opacity-100" ')

html_path = "vehicle_lab_vanilla/helix.html"
with open(html_path, "r") as f:
    html_content = f.read()

target = '<!-- Data Pipeline Section -->'
replacement = f"""
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
            
            <div class="glass-cyber rounded-3xl border border-white/5 p-4 md:p-12 shadow-2xl shadow-neon-purple/10 flex justify-center w-full transform hover:scale-[1.01] transition-transform duration-500 bg-slate-900/50 backdrop-blur-xl">
                {{{{SVG}}}}
            </div>
        </div>
    </section>

    <!-- Data Pipeline Section -->"""

# Perform replacement
replacement = replacement.replace('{{SVG}}', svg_styled)
if target in html_content:
    new_html = html_content.replace(target, replacement)
    # The previous Data Pipeline section also had a border-t border-slate-800. We can remove it so there are no double horizontal lines.
    new_html = new_html.replace('<section class="py-32 border-t border-slate-800 bg-[#050508]" id="data">', '<section class="py-32 bg-[#050508]" id="data">')
    with open(html_path, "w") as f:
        f.write(new_html)
    print("SVG inserted successfully.")
else:
    print("Error: Target not found.")
