import re

svg_path = "pics/cie.svg"
with open(svg_path, "r") as f:
    svg_content = f.read()

# 1. Hide the Napkin logo
svg_content = svg_content.replace('fill="#ababab88"', 'fill="none" display="none"')

# 2. Make SVG scalable and huge, matching the helix aesthetic
# Use scale-[1.3] md:scale-[1.6] initially, this might need tuning.
new_svg_class = 'class="w-full max-w-none mx-auto drop-shadow-2xl opacity-90 transition-all duration-700 hover:opacity-100 transform scale-[1.35] md:scale-[1.6] origin-top -mt-4" '
svg_content = svg_content.replace('<svg ', f'<svg {new_svg_class} ')

# 3. Remove the exact title string ONLY, leave structure intact
svg_content = svg_content.replace("CIE Pro's Core Capabilities", '')

# Adjust viewBox to crop the top blank space where title was
svg_content = svg_content.replace('viewBox="0 0 546 413"', 'viewBox="0 30 546 383"')

html_path = "vehicle_lab_vanilla/cie_pro.html"
with open(html_path, "r") as f:
    html_content = f.read()

new_section = f"""
    <!-- Visually Stunning Workflow Diagram Section -->
    <section class="py-24 border-t border-slate-800 relative bg-[#030305] overflow-hidden">
        <!-- Background Accents -->
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-4xl h-px bg-gradient-to-r from-transparent via-cyan-500/50 to-transparent"></div>
        <div class="absolute -top-32 left-1/2 -translate-x-1/2 w-[800px] h-[300px] bg-cyan-500/5 blur-[120px] rounded-full point-events-none"></div>
        
        <div class="max-w-[1400px] mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="text-center mb-16">
                <h2 class="text-cyan-500 font-bold tracking-widest uppercase text-sm mb-4 animate-pulse">Core Intelligence Engine</h2>
                <h3 class="text-3xl md:text-5xl font-bold text-white mb-6">CIE Pro Architecture</h3>
                <p class="text-slate-400 max-w-3xl mx-auto text-lg">
                    Advanced optimization through surrogate modeling, physics-informed AI, and seamless ASAM toolchain integration.
                </p>
            </div>
            
            <div class="glass-cyber rounded-3xl border border-white/5 p-8 md:p-16 pb-24 md:pb-40 pt-4 md:pt-8 shadow-2xl shadow-cyan-500/10 flex justify-center w-full transform hover:scale-[1.01] transition-transform duration-500 bg-slate-900/50 backdrop-blur-xl">
                {svg_content}
            </div>
        </div>
    </section>
    
    <!-- Physics-Informed Intelligence Section -->"""

# Inject before Physics-Informed
html_content = html_content.replace('<!-- Physics-Informed Intelligence Section -->', new_section)

with open(html_path, "w") as f:
    f.write(html_content)

print("Injected CIE SVG successfully.")
