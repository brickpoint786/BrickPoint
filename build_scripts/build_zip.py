import os, zipfile

SOURCE_DIR = "/home/user/BrickPoint/wordpress/brickpoint"
ZIP_DESTS = [
    "/home/user/BrickPoint/brickpoint-wordpress-elementor-final-v2.zip",
    "/home/user/brickpoint-wordpress-elementor-final-v2.zip",
    "/home/user/BrickPoint/brickpoint-wordpress-elementor-final.zip",
    "/home/user/brickpoint-wordpress-elementor-final.zip"
]

for zip_dest in ZIP_DESTS:
    if os.path.exists(zip_dest):
        os.remove(zip_dest)

    with zipfile.ZipFile(zip_dest, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(SOURCE_DIR):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, os.path.dirname(SOURCE_DIR))
                zipf.write(full_path, rel_path)

    size_kb = os.path.getsize(zip_dest) / 1024
    print(f"Created {zip_dest} ({size_kb:.1f} KB)")

# Verify zip archive structure
with zipfile.ZipFile(ZIP_DESTS[0], "r") as z:
    infolist = z.infolist()
    print(f"Total files in zip: {len(infolist)}")
    for f in infolist[:8]:
        print("  Sample file:", f.filename)
    has_style = any(f.filename == "brickpoint/style.css" for f in infolist)
    has_functions = any(f.filename == "brickpoint/functions.php" for f in infolist)
    has_templates = any(f.filename == "brickpoint/elementor-templates/page-home.json" for f in infolist)
    print(f"Verification: brickpoint/style.css present? {has_style}")
    print(f"Verification: brickpoint/functions.php present? {has_functions}")
    print(f"Verification: brickpoint/elementor-templates/page-home.json present? {has_templates}")
