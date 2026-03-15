import os
import shutil

# Configuration
BASE_DIR = "/Users/chayan/Documents/web_deploy_res"
SOURCE_MAP = {
    "DiagAI": "diagai",
    "CIE/app/docs": "cie",
    "HELIX": "helix"
}

def consolidate_files():
    print(f"Starting consolidation in {BASE_DIR}")
    
    for source_subpath, prefix in SOURCE_MAP.items():
        source_dir = os.path.join(BASE_DIR, source_subpath)
        
        if not os.path.exists(source_dir):
            print(f"Warning: Source directory {source_dir} not found. Skipping.")
            continue
            
        print(f"Processing {source_dir} -> {prefix}...")
        
        # Get list of files
        try:
            files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
            files.sort() # Ensure deterministic order
        except OSError as e:
            print(f"Error accessing {source_dir}: {e}")
            continue

        count = 0
        for i, filename in enumerate(files, 1):
            if filename == ".DS_Store":
                continue
                
            original_path = os.path.join(source_dir, filename)
            new_filename = f"{prefix}_{i}_{filename}"
            new_path = os.path.join(BASE_DIR, new_filename)
            
            try:
                # Copy instead of move first to be safe, or just move? Plan said move.
                # Let's move.
                shutil.move(original_path, new_path)
                print(f"Moved: {filename} -> {new_filename}")
                count += 1
            except Exception as e:
                print(f"Failed to move {filename}: {e}")
        
        print(f"Finished {prefix}: {count} files moved.\n")

    print("Consolidation complete.")

if __name__ == "__main__":
    consolidate_files()
