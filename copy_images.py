import shutil
import os

source_dir = "/Users/paulsonornot/.gemini/antigravity/brain/fc9315c3-f577-462b-929f-500d7d35011e"
dest_dir = "/Volumes/Data/Курсы/AI/Programming/01 Landinng/images"

files = [
    "hero_bg_1763661679321.png",
    "about_img_1763661688025.png",
    "tourn_novice_1763661694797.png",
    "tourn_pro_1763661702200.png",
    "tourn_cup_1763661726179.png",
    "gallery_1_1763661732981.png",
    "gallery_2_1763661742618.png",
    "gallery_3_1763661750148.png",
    "gallery_4_1763661757071.png"
]

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
    print(f"Created directory: {dest_dir}")

for f in files:
    src = os.path.join(source_dir, f)
    dst = os.path.join(dest_dir, f)
    try:
        shutil.copy2(src, dst)
        print(f"Copied {f}")
    except Exception as e:
        print(f"Error copying {f}: {e}")
