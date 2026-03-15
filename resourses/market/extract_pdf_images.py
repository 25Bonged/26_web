import fitz
import os

pdf_groups = {
    'diagai': [
        'DiagAI_Senior_Engineer_In_The_Machine.pdf',
        'Diagnostic_Intelligence_Redefined.pdf'
    ],
    'ciepro': [
        'CIE.pdf'
    ],
    'helix': [
        'HELIX_2.0_Strategic_Pivot.pdf',
        'HELIX_Calibration_Ecosystem.pdf',
        'HELIX_Calibration_Lifecycle_Management.pdf',
        'The_Intelligence_Era_of_Calibration.pdf'
    ],
    'automotive': [
        'Automotive_Intelligence_Ecosystem (1).pdf',
        'Automotive_Software_Ecosystem_The_Next_Generation.pdf'
    ]
}

def extract_images(pdf_list, prefix):
    for pdf_idx, pdf_filename in enumerate(pdf_list, start=1):
        if not os.path.exists(pdf_filename):
            print(f"File not found: {pdf_filename}")
            continue
        try:
            doc = fitz.open(pdf_filename)
        except Exception as e:
            print(f"Error opening {pdf_filename}: {e}")
            continue
            
        for page_idx in range(len(doc)):
            page = doc[page_idx]
            image_list = page.get_images(full=True)
            
            # Format: prefix_pdfIdx_pageIdx
            base_name = f"{prefix}_{pdf_idx}_{page_idx + 1}"
            
            if not image_list:
                # Render the page
                pix = page.get_pixmap(dpi=300)
                image_filename = f"{base_name}.png"
                pix.save(image_filename)
                print(f"Saved {image_filename} (Rendered)")
            else:
                for img_idx, img in enumerate(image_list):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    img_ext = base_image["ext"]
                    
                    if len(image_list) == 1:
                        image_filename = f"{base_name}.{img_ext}"
                    else:
                        image_filename = f"{base_name}_{img_idx + 1}.{img_ext}"
                        
                    with open(image_filename, "wb") as f:
                        f.write(image_bytes)
                    print(f"Saved {image_filename}")

if __name__ == '__main__':
    for prefix, pdf_list in pdf_groups.items():
        extract_images(pdf_list, prefix)
