import zlib, struct, os, math

def create_png_with_drawing(width, height, draw_func):
    png = b'\x89PNG\r\n\x1a\n'
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    ihdr_crc = struct.pack('>I', zlib.crc32(b'IHDR' + ihdr_data) & 0xffffffff)
    png += struct.pack('>I', len(ihdr_data)) + b'IHDR' + ihdr_data + ihdr_crc

    raw_rows = []
    for y in range(height):
        row = bytearray([0])
        for x in range(width):
            r, g, b = draw_func(x, y, width, height)
            row.append(max(0, min(255, int(r))))
            row.append(max(0, min(255, int(g))))
            row.append(max(0, min(255, int(b))))
        raw_rows.append(bytes(row))
    raw = b''.join(raw_rows)
    idat_data = zlib.compress(raw, 6)
    idat_crc = struct.pack('>I', zlib.crc32(b'IDAT' + idat_data) & 0xffffffff)
    png += struct.pack('>I', len(idat_data)) + b'IDAT' + idat_data + idat_crc

    iend_crc = struct.pack('>I', zlib.crc32(b'IEND') & 0xffffffff)
    png += struct.pack('>I', 0) + b'IEND' + iend_crc
    return png

def draw_screenshot(x, y, w, h):
    # Header area (0 to 60)
    if y < 60:
        if y < 4:
            return 234, 88, 12 # orange top line
        return 20, 18, 16 # dark header
    
    # Hero area (60 to 380)
    if y < 380:
        # brick lines subtle pattern
        bx = (x + (0 if (y // 18) % 2 == 0 else 24)) % 48
        by = y % 18
        is_mortar = bx < 2 or by < 2
        
        # vignette / gradient
        grad = (y - 60) / 320.0
        base_r = int(28 + grad * 10)
        base_g = int(26 + grad * 8)
        base_b = int(23 + grad * 6)
        
        # right side featured card / orange glow
        if 480 < x < 740 and 100 < y < 340:
            if x == 481 or x == 739 or y == 101 or y == 339:
                return 234, 88, 12
            return int(36 + (x - 480)*0.1), 32, 28

        if is_mortar:
            return base_r + 15, base_g + 12, base_b + 10
        return base_r, base_g, base_b

    # Lower section: white / sand content area with cards
    # Marquee bar (380 to 410)
    if y < 410:
        return 234, 88, 12

    # Cards grid (410 to 600)
    # Background sand
    bg_r, bg_g, bg_b = 250, 248, 245
    
    # 4 Cards: x ranges
    # card 1: 40-200, card 2: 220-380, card 3: 400-560, card 4: 580-740
    card_y1, card_y2 = 430, 580
    for cx in [40, 220, 400, 580]:
        if cx <= x <= cx + 180 and card_y1 <= y <= card_y2:
            # Card border
            if x == cx or x == cx + 180 or y == card_y1 or y == card_y2:
                return 220, 215, 205
            # Card image area (top half of card)
            if y < card_y1 + 80:
                # terracotta brick image
                bx = (x + (0 if (y // 12) % 2 == 0 else 16)) % 32
                by = y % 12
                if bx < 2 or by < 2:
                    return 200, 190, 180
                return 194, 65, 12
            # Card text area
            if y > card_y2 - 25:
                # Green WhatsApp button
                if cx + 20 <= x <= cx + 160:
                    return 18, 140, 75
            return 255, 255, 255
            
    return bg_r, bg_g, bg_b

out_path = "/home/user/BrickPoint/wordpress/brickpoint/screenshot.png"
png_bytes = create_png_with_drawing(800, 600, draw_screenshot)
with open(out_path, "wb") as f:
    f.write(png_bytes)

print(f"Generated {out_path} ({len(png_bytes)} bytes)")
