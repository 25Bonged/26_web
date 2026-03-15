import re

def fix_html(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # 1. Reduce extreme scaling that causes layout overflow
    # Helix and CIE both use 1.35/1.6 currently
    content = content.replace('scale-[1.35] md:scale-[1.6]', 'scale-[1.15] md:scale-[1.3]')
    
    # 2. Add overflow-hidden to the glass containers to prevent bleed-out
    # Pattern to find glass-cyber containers holding SVGs
    # Specifically looking for the ones containing the SVGs we added
    content = content.replace('glass-cyber rounded-3xl border border-white/5 p-8 md:p-16', 'glass-cyber rounded-3xl border border-white/5 overflow-hidden p-8 md:p-16')
    content = content.replace('glass-cyber rounded-3xl border border-white/5 p-8 md:p-24', 'glass-cyber rounded-3xl border border-white/5 overflow-hidden p-8 md:p-24')
    
    # 3. Add max-height limit to the SVGs to keep them from being taller than the screen
    # Adding 'max-h-[70vh]' to existing SVG classes
    content = content.replace('w-full max-w-none mx-auto drop-shadow-2xl', 'w-full max-w-none max-h-[70vh] mx-auto drop-shadow-2xl')

    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Fixed scaling and overflow in {file_path}")

fix_html('vehicle_lab_vanilla/cie_pro.html')
fix_html('vehicle_lab_vanilla/helix.html')
