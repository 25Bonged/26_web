import os
from bs4 import BeautifulSoup

BASE_DIR = '/Users/chayan/Documents/web_deploy_res/vehicle_lab_vanilla'
TARGET_DIR = '/Users/chayan/Documents/web_deploy_res/vehicle_lab_multi_page'

pages = {
    'index': ('vehicle lab', 'index.html'),
    'solutions': ('solutions', None),
    'cie_pro': ('solutions', 'cie_pro.html'),
    'diagai': ('solutions', 'diagai.html'),
    'helix': ('solutions', 'helix.html'),
    'contact_us': ('more_info', 'contact_us.html'),
    'case_studies': ('more_info', 'case_studies.html'),
    'docs': ('docs', 'docs.html'),
    'pricing': ('pricing', 'pricing.html'),
}

# The new HTML navigation template for all pages
NAV_HTML = """
<nav class="fixed w-full z-50 bg-[#0a0a0a]/80 backdrop-blur-md border-b border-white/5 transition-all duration-300">
  <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
    <a href="index.html" class="flex items-center gap-3 group">
      <div class="w-6 h-6 rounded flex items-center justify-center bg-white text-black transition-transform group-hover:scale-105">
        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
      </div>
      <span class="font-medium text-lg tracking-tight text-white group-hover:text-slate-300 transition-colors">Vehicle Lab</span>
    </a>
    
    <div class="hidden md:flex items-center gap-6 text-sm font-medium text-slate-400">
      <!-- Solutions Dropdown -->
      <div class="relative group cursor-pointer inline-block py-6">
        <span class="hover:text-white transition-colors flex items-center gap-1">Products <svg class="w-3 h-3 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></span>
        <div class="absolute top-[100%] left-0 w-48 bg-[#111] border border-white/10 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 py-2">
          <a href="diagai.html" class="block px-4 py-2 hover:bg-white/5 hover:text-white transition-colors">DiagAI</a>
          <a href="cie_pro.html" class="block px-4 py-2 hover:bg-white/5 hover:text-white transition-colors">CIE Pro</a>
          <a href="helix.html" class="block px-4 py-2 hover:bg-white/5 hover:text-white transition-colors">HELIX</a>
        </div>
      </div>
      
      <a href="pricing.html" class="hover:text-white transition-colors">Pricing</a>
      <a href="docs.html" class="hover:text-white transition-colors">Docs</a>
    </div>
    
    <div class="flex items-center gap-4">
      <a href="contact_us.html" class="hidden lg:block text-sm font-medium text-slate-400 hover:text-white transition-colors">Contact Engineering</a>
      <a href="contact_us.html" class="bg-white hover:bg-slate-200 text-black px-4 py-1.5 rounded-md text-sm font-medium transition-all shadow-sm">Talk to Sales</a>
    </div>
  </div>
</nav>
"""

def generate_base_html(title):
    return f"""<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Vehicle Lab</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/geist@1.0.0/dist/fonts/geist-sans/style.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <script id="tailwind-config">tailwind.config = {{
        darkMode: "class",
        theme: {{
            extend: {{
                colors: {{
                    "primary": "#ededed",
                    "neon-blue": "#0070f3",
                    "neon-green": "#10b981",
                    "neon-purple": "#8b5cf6",
                    "background-light": "#ffffff",
                    "background-dark": "#0a0a0a",
                }},
                fontFamily: {{
                    "display": ["Geist", "sans-serif"],
                    "sans": ["Geist", "sans-serif"],
                    "mono": ["JetBrains Mono", "monospace"]
                }},
            }},
        }},
    }}</script>
    <style>
        body {{ font-family: 'Geist', sans-serif; background-color: #0a0a0a; color: #ededed; overflow-x: hidden; }}
        ::selection {{ background-color: #333; color: white; }}
        .material-symbols-outlined {{ font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 24; }}
        
        /* Subdued Glows (10-15% opacity) */
        .glow-text-blue {{ text-shadow: 0 0 10px rgba(0, 112, 243, 0.15); }}
        .glow-text-green {{ text-shadow: 0 0 10px rgba(16, 185, 129, 0.15); }}
        .glow-text-purple {{ text-shadow: 0 0 10px rgba(139, 92, 246, 0.15); }}
        
        /* Subtle Borders with reveal on hover */
        .neon-border-blue {{ border: 1px solid rgba(255,255,255,0.05); transition: border-color 0.2s ease; }}
        .neon-border-blue:hover {{ border-color: rgba(0, 112, 243, 0.4); }}
        .neon-border-green {{ border: 1px solid rgba(255,255,255,0.05); transition: border-color 0.2s ease; }}
        .neon-border-green:hover {{ border-color: rgba(16, 185, 129, 0.4); }}
        .neon-border-purple {{ border: 1px solid rgba(255,255,255,0.05); transition: border-color 0.2s ease; }}
        .neon-border-purple:hover {{ border-color: rgba(139, 92, 246, 0.4); }}
        
        /* Subtle Grid */
        .cyber-grid {{ background-image: radial-gradient(circle at 1px 1px, rgba(255, 255, 255, 0.05) 1px, transparent 0); background-size: 40px 40px; }}
        
        /* Glass Panels */
        .glass-cyber {{ background: rgba(255, 255, 255, 0.02); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.05); }}
        .glass-panel {{ background: rgba(10, 10, 10, 0.8); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.05); }}
        .glass-card {{ background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); transition: background 0.2s ease, border-color 0.2s ease; }}
        .glass-card:hover {{ background: rgba(255, 255, 255, 0.04); border-color: rgba(255, 255, 255, 0.1); }}
        
        .neon-glow {{ filter: drop-shadow(0 0 4px rgba(255,255,255,0.1)); }}
        
        /* Smooth transitions */
        * {{ transition-duration: 200ms; }}
    </style>
</head>
<body class="antialiased bg-background-dark text-white cyber-grid selection:bg-white/20">
    {NAV_HTML}
    <main class="pt-16">
        <!-- Content gets injected here -->
    </main>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            AOS.init({{
                duration: 400, // Faster animations
                once: true,
                offset: 20,
                easing: 'ease-out'
            }});
        }});
    </script>
</body>
</html>"""

for page_id, (category, relative_path) in pages.items():
    if not relative_path:
        # Generate placeholder bridging pages for solutions and more_info
        html_content = generate_base_html(page_id.replace('_', ' ').title())
        soup = BeautifulSoup(html_content, 'html.parser')
        main = soup.find('main')
        
        # Build placeholder section
        section = soup.new_tag('section', **{'class': 'py-32 px-6 max-w-7xl mx-auto text-center'})
        h1 = soup.new_tag('h1', **{'class': 'text-5xl font-black mb-6'})
        h1.string = page_id.replace('_', ' ').title()
        p = soup.new_tag('p', **{'class': 'text-xl text-slate-400 mb-12'})
        p.string = "Explore our specific offerings below."
        
        links_div = soup.new_tag('div', **{'class': 'flex justify-center gap-4'})
        if page_id == 'solutions':
            l1 = soup.new_tag('a', href='diagai.html', **{'class': 'bg-slate-800 px-6 py-3 rounded-xl hover:bg-slate-700 font-bold text-[#39ff14]'})
            l1.string = "DiagAI"
            l2 = soup.new_tag('a', href='cie_pro.html', **{'class': 'bg-slate-800 px-6 py-3 rounded-xl hover:bg-slate-700 font-bold text-[#22d3ee]'})
            l2.string = "CIE Pro"
            l3 = soup.new_tag('a', href='helix.html', **{'class': 'bg-slate-800 px-6 py-3 rounded-xl hover:bg-slate-700 font-bold text-[#a855f7]'})
            l3.string = "HELIX"
            links_div.extend([l1, l2, l3])
        elif page_id == 'more_info':
            l1 = soup.new_tag('a', href='about_us.html', **{'class': 'bg-slate-800 px-6 py-3 rounded-xl hover:bg-slate-700 font-bold text-white'})
            l1.string = "About Us"
            l2 = soup.new_tag('a', href='contact_us.html', **{'class': 'bg-slate-800 px-6 py-3 rounded-xl hover:bg-slate-700 font-bold text-white'})
            l2.string = "Contact Us"
            l3 = soup.new_tag('a', href='case_studies.html', **{'class': 'bg-slate-800 px-6 py-3 rounded-xl hover:bg-slate-700 font-bold text-white'})
            l3.string = "Case Studies"
            links_div.extend([l1, l2, l3])
            
        section.append(h1)
        section.append(p)
        section.append(links_div)
        main.append(section)
        
        # Inject animations
        for i, element in enumerate(soup.find_all(['h1', 'p', 'a'])):
            if not element.has_attr('data-aos') and not element.find_parent('nav'):
                element['data-aos'] = 'fade-up'
                element['data-aos-delay'] = str((i % 4) * 100)
        
        output_file = os.path.join(TARGET_DIR, f"{page_id}.html")
        with open(output_file, 'w') as out:
            out.write(str(soup))
        continue
        
    full_path = os.path.join(BASE_DIR, relative_path)
    if not os.path.exists(full_path):
        print(f"Warning: {full_path} not found. Skipping {page_id}.html")
        continue

    # Standalone pages that don't need generate_base_html wrapping
    if page_id == 'docs':
        with open(full_path, 'r') as f:
            content = f.read()
        
        # Inject the global navigation into the standalone page
        content = content.replace('{NAV_HTML}', NAV_HTML)
        
        output_file = os.path.join(TARGET_DIR, f"{page_id}.html")
        with open(output_file, 'w') as out:
            out.write(content)
        continue
        
    # Read the source file
    with open(full_path, 'r') as f:
        source_soup = BeautifulSoup(f.read(), 'html.parser')

    # Start with a fresh base layout
    base_html = generate_base_html(page_id.replace('_', ' ').title())
    out_soup = BeautifulSoup(base_html, 'html.parser')
    main_tag = out_soup.find('main')
    
    # Extract sections to copy into main
    source_main = source_soup.find('main')
    content_tags = []
    
    if source_main:
        # Get all immediate children of main that aren't nav/footer
        content_tags = [tag for tag in source_main.find_all(recursive=False) if tag.name not in ('nav', 'header', 'footer', 'script')]
    else:
        # Fallback: find all top-level sections or large divs in the body
        body = source_soup.find('body')
        if body:
            # Look for sections first
            content_tags = body.find_all(['section', 'script'], recursive=False)
            if not content_tags:
                # If no sections at root of body, look for all divs that aren't nav/footer
                # We want to keep scripts!
                content_tags = [tag for tag in body.find_all(recursive=False) if tag.name not in ('nav', 'header', 'footer')]
        else:
            # Absolute fallback if no body tag (fragment)
            content_tags = [tag for tag in source_soup.find_all(recursive=False) if tag.name not in ('nav', 'header', 'footer', 'script', 'html', 'head')]

    for tag in content_tags:
        main_tag.append(tag)
        
    # Auto-inject AOS animations for premium interactivity
    # Only animate container sections and cards, NOT individual text elements
    # (text AOS causes above-fold content to be invisible on page load, breaking layout)
    for i, section_div in enumerate(out_soup.find_all('section')):
        if not section_div.has_attr('data-aos') and not section_div.find_parent('nav'):
            section_div['data-aos'] = 'fade-up'
            section_div['data-aos-delay'] = '0'
            
    for i, div in enumerate(
        out_soup.find_all('div', class_=lambda c: c and 
            any(cls in c for cls in ['rounded-2xl', 'rounded-3xl', 'rounded-[2rem]', 'rounded-[2.5rem]', 'rounded-[3rem]']))
    ):
        if not div.has_attr('data-aos') and not div.find_parent('nav'):
            div['data-aos'] = 'fade-up'
            div['data-aos-delay'] = str((i % 4) * 100)
        
    output_file = os.path.join(TARGET_DIR, f"{page_id}.html")
    with open(output_file, 'w') as out:
         out.write(str(out_soup))

print("Created multi-page site successfully with premium animations.")
