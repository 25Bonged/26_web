import os
from bs4 import BeautifulSoup

BASE_DIR = '/Users/chayan/Documents/web_deploy_res/stitch_vehicle_lab_landing_page'
TARGET_FILE = '/Users/chayan/Documents/web_deploy_res/vehicle_lab_vanilla/index.html'

files_to_merge = [
    ('landing', 'landing_page:_blue_ai_workflow/code.html'),
    ('cie_pro', '../vehicle_lab_vanilla/cie_pro.html'),
    ('diagai', '../vehicle_lab_vanilla/diagai.html'),
    ('helix', 'helix:_neon-futuristic_detail/code.html'),
    ('pricing', 'pricing_with_enterprise_comparison/code.html'),
    ('about_us', 'about_us:_neon-futuristic_rebrand/code.html'),
    ('contact_us', '../vehicle_lab_vanilla/contact_us.html'),
    ('case_studies', '../vehicle_lab_vanilla/case_studies.html'),
]

# Read base landing page as our foundation
base_html_path = os.path.join(BASE_DIR, files_to_merge[0][1])
with open(base_html_path, 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

main_tag = soup.find('main')
if not main_tag:
    print("No main tag found in base HTML")
    exit(1)

# Add section IDs to existing sections in base if they don't have one
for tag in main_tag.find_all('section', recursive=False):
    if not tag.has_attr('id'):
        tag['id'] = 'hero' # Assuming first section is hero

# Create wrapper divs for our major tabs to handle smooth scrolling better
solutions_wrapper = soup.new_tag('div', id='solutions')
pricing_wrapper = soup.new_tag('div', id='pricing')
more_info_wrapper = soup.new_tag('div', id='more-info')

main_tag.append(solutions_wrapper)
main_tag.append(pricing_wrapper)
main_tag.append(more_info_wrapper)


for label, filename in files_to_merge[1:]:
    filepath = os.path.join(BASE_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            section_soup = BeautifulSoup(f, 'html.parser')
            
            # Extract main content (everything inside <main> or <body> excluding nav/footer)
            section_main = section_soup.find('main')
            if section_main:
                content_tags = section_main.find_all('section', recursive=False)
            else:
                body = section_soup.find('body')
                if body:
                    content_tags = [tag for tag in body.find_all(recursive=False) if tag.name not in ('nav', 'header', 'footer', 'script')]
                else:
                    # If there's no body, it's just raw HTML tags like <section>
                    content_tags = [tag for tag in section_soup.find_all(recursive=False) if tag.name not in ('nav', 'header', 'footer', 'script')]

            for tag in content_tags:
                if label in ('cie_pro', 'diagai', 'helix'):
                    tag['id'] = f"solution-{label}"
                    solutions_wrapper.append(tag)
                elif label == 'pricing':
                    tag['id'] = "section-pricing"
                    pricing_wrapper.append(tag)
                elif label in ('about_us', 'contact_us', 'case_studies'):
                    tag['id'] = f"more-info-{label}"
                    more_info_wrapper.append(tag)
                else:
                    main_tag.append(tag)
    else:
        print(f"Warning: {filepath} not found.")

# Update the navbar links to point to these new sections
nav = soup.find('nav')
if nav:
    # Update navigation links
    links = nav.find_all('a')
    nav_map = {
        'CIE Pro': '#solution-cie_pro',
        'DiagAI': '#solution-diagai',
        'HELIX': '#solution-helix',
        'Solutions': '#solutions'
    }
    
    # We will rebuild the nav container to include all required tabs smoothly
    nav_links_container = None
    for link in links:
        if 'hover:text-primary' in link.get('class', []):
            text = link.text.strip()
            if text in nav_map:
                link['href'] = nav_map[text]
            nav_links_container = link.parent # roughly get the container
    
    if nav_links_container:
        # Add new links for Pricing and More Info
        pricing_link = soup.new_tag('a', href='#section-pricing', **{'class': 'text-sm font-semibold hover:text-primary transition-colors uppercase tracking-wider'})
        pricing_link.string = 'Pricing'
        
        more_info_link = soup.new_tag('a', href='#more-info', **{'class': 'text-sm font-semibold hover:text-primary transition-colors uppercase tracking-wider'})
        more_info_link.string = 'More Info'
        
        div_sep = soup.new_tag('div', **{'class': 'h-4 w-[1px] bg-white/10'})
        nav_links_container.append(div_sep)
        nav_links_container.append(pricing_link)
        nav_links_container.append(more_info_link)

# Add smooth scrolling JS
script_tag = soup.new_tag('script')
script_tag.string = """
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            const target = document.querySelector(targetId);
            if(target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
"""
soup.body.append(script_tag)

# Set smooth scrolling in CSS
style_tag = soup.new_tag('style')
style_tag.string = "html { scroll-behavior: smooth; }"
soup.head.append(style_tag)

with open(TARGET_FILE, 'w') as f:
    f.write(str(soup))

print("Merge complete.")
