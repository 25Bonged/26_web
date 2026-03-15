import os
import re
from bs4 import BeautifulSoup

TARGET_FILES = [
    'index.html',
    'cie_pro.html',
    'diagai.html',
    'helix.html'
]

def apply_theme(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Remove manual neon hex colors and replace with semantic tailwind config colors
    content = content.replace('bg-[#39ff14]', 'bg-neon-green')
    content = content.replace('text-[#39ff14]', 'text-neon-green')
    content = content.replace('border-[#39ff14]/', 'border-neon-green/')
    content = content.replace('shadow-[0_0_20px_rgba(57,255,20,0.3)]', 'shadow-lg shadow-neon-green/10')
    content = content.replace('shadow-[0_0_50px_rgba(57,255,20,0.1)]', 'shadow-xl shadow-neon-green/5')

    content = content.replace('bg-[#00f3ff]', 'bg-neon-blue')
    content = content.replace('text-[#00f3ff]', 'text-neon-blue')
    
    content = content.replace('bg-[#bc13fe]', 'bg-neon-purple')
    content = content.replace('text-[#bc13fe]', 'text-neon-purple')
    
    # 2. Quiet down the typography (remove uppercase and wide tracking)
    content = re.sub(r'\buppercase\s+tracking-widest\b', 'font-medium tracking-tight', content)
    content = re.sub(r'\buppercase\s+tracking-\[.*?\]\b', 'font-medium tracking-tight', content)
    content = re.sub(r'\bfont-black\b', 'font-bold', content)
    
    # Remove all glows
    content = re.sub(r'\bglow-text-(blue|green|purple)\b', '', content)
    
    # 3. Increase padding and whitespace for 'Information Density'
    content = content.replace('py-24 ', 'py-32 ')
    content = content.replace('p-8 ', 'p-10 ')
    content = content.replace('p-10 ', 'p-14 ')
    content = content.replace('p-12 ', 'p-16 ')
    content = content.replace('gap-8 ', 'gap-12 ')
    
    # 4. Tone down borders/backgrounds
    content = content.replace('border-primary/20', 'border-white/5')
    content = content.replace('border-neon-green/20', 'border-white/5')
    content = content.replace('border-neon-purple/20', 'border-white/5')
    content = content.replace('bg-primary/20', 'bg-primary/5')
    content = content.replace('bg-primary/10', 'bg-primary/5')
    content = content.replace('blur-[100px]', 'blur-[80px]')
    content = content.replace('blur-[120px]', 'blur-[80px]')
    content = content.replace('blur-[150px]', 'blur-[100px]')

    # Clean up multiple spaces
    content = re.sub(r' {2,}', ' ', content)

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Successfully applied theme to {filepath}")

if __name__ == '__main__':
    for file in TARGET_FILES:
        apply_theme(file)
