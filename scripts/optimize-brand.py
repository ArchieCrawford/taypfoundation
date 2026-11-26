#!/usr/bin/env python3
"""Build web-sized logo, favicon, Open Graph, and grain assets."""

from pathlib import Path

from PIL import Image, ImageFilter, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
UPLOADS = Path("/home/ubuntu/.cursor/projects/workspace/uploads")
BLACK = UPLOADS / "tayp_foundation_logo_black_1ca5.png"
TRANS = UPLOADS / "tayp_foundation_logo_transparent_07c6.png"
PUBLIC = ROOT / "public"
BRAND = PUBLIC / "brand"
TEXTURES = PUBLIC / "textures"


def content_bbox(im: Image.Image, alpha_min: int = 12) -> tuple[int, int, int, int]:
    rgba = im.convert("RGBA")
    px = rgba.load()
    w, h = rgba.size
    minx, miny, maxx, maxy = w, h, 0, 0
    for y in range(h):
        for x in range(w):
            if px[x, y][3] > alpha_min:
                minx = min(minx, x)
                miny = min(miny, y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)
    return minx, miny, maxx + 1, maxy + 1


def key_near_black(im: Image.Image, threshold: int = 22) -> Image.Image:
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            peak = max(r, g, b)
            if peak <= threshold:
                px[x, y] = (r, g, b, 0)
            elif peak < threshold + 28:
                fade = (peak - threshold) / 28
                px[x, y] = (r, g, b, int(a * fade))
    return im


def square_on_black(im: Image.Image, padding_ratio: float = 0.12) -> Image.Image:
    im = im.convert("RGBA")
    # Trim fully transparent edges after keying.
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    side = max(im.size)
    pad = int(side * padding_ratio)
    canvas_side = side + pad * 2
    canvas = Image.new("RGBA", (canvas_side, canvas_side), (7, 7, 7, 255))
    ox = (canvas_side - im.size[0]) // 2
    oy = (canvas_side - im.size[1]) // 2
    canvas.alpha_composite(im, (ox, oy))
    return canvas.convert("RGB")


def resize(im: Image.Image, width: int) -> Image.Image:
    height = round(im.size[1] * width / im.size[0])
    return im.resize((width, height), Image.Resampling.LANCZOS)


def flatten_on_black(im: Image.Image) -> Image.Image:
    bg = Image.new("RGBA", im.size, (7, 7, 7, 255))
    return Image.alpha_composite(bg, im.convert("RGBA")).convert("RGB")


def steel_background(size: tuple[int, int]) -> Image.Image:
    """Near-black field with a light horizontal brush, not a brown wash."""
    w, h = size
    base = Image.new("RGB", size, (7, 7, 7))
    noise = Image.effect_noise((w, h), 14).convert("L")
    noise = noise.filter(ImageFilter.BoxBlur(0.4))
    # Keep the grain in a tight band around black so the field stays black.
    noise = noise.point(lambda p: 4 + (p * 22) // 255)
    noise_rgb = Image.merge("RGB", (noise, noise, noise))
    base = Image.blend(base, noise_rgb, 0.85)
    streaks = Image.new("RGBA", size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(streaks)
    for y in range(0, h, 2):
        alpha = 18 if (y // 2) % 3 == 0 else 6
        sd.line([(0, y), (w, y)], fill=(210, 214, 220, alpha), width=1)
    out = Image.alpha_composite(base.convert("RGBA"), streaks).convert("RGB")
    rule = ImageDraw.Draw(out)
    rule.rectangle((0, h - 6, w, h), fill=(247, 120, 30))
    return out


def main() -> None:
    BRAND.mkdir(parents=True, exist_ok=True)
    TEXTURES.mkdir(parents=True, exist_ok=True)

    transparent = Image.open(TRANS).convert("RGBA")
    bbox = content_bbox(transparent, 18)
    # Keep a little of the brushed edge.
    pad = 12
    w, h = transparent.size
    crop_box = (
        max(0, bbox[0] - pad),
        max(0, bbox[1] - pad),
        min(w, bbox[2] + pad),
        min(h, bbox[3] + pad),
    )
    logo_rgba = transparent.crop(crop_box)
    logo_flat = flatten_on_black(logo_rgba)
    logo_web = resize(logo_rgba, 880)
    # The painted tagline sits under the silver rule. The hero repeats it in HTML.
    logo_web = logo_web.crop((0, 0, logo_web.size[0], round(logo_web.size[1] * 686 / 730)))
    logo_web.save(BRAND / "logo.webp", "WEBP", quality=76, method=6, alpha_quality=50)

    black = Image.open(BLACK).convert("RGB")
    # TT monogram band measured from the master artwork.
    mark = black.crop((337, 148, 913, 592))
    mark = key_near_black(mark, 18)
    mark_sq = square_on_black(mark, 0.14)
    mark_sq.resize((512, 512), Image.Resampling.LANCZOS).save(PUBLIC / "icon-512.png", "PNG", optimize=True)
    mark_sq.resize((192, 192), Image.Resampling.LANCZOS).save(PUBLIC / "icon-192.png", "PNG", optimize=True)
    mark_sq.resize((180, 180), Image.Resampling.LANCZOS).save(PUBLIC / "apple-touch-icon.png", "PNG", optimize=True)
    mark_sq.resize((32, 32), Image.Resampling.LANCZOS).save(PUBLIC / "favicon-32.png", "PNG", optimize=True)
    mark_sq.save(
        PUBLIC / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
    )

    nav_mark = mark_sq.resize((160, 160), Image.Resampling.LANCZOS)
    nav_mark.save(BRAND / "mark.png", "PNG", optimize=True)
    nav_mark.save(BRAND / "mark.webp", "WEBP", quality=82, method=6)

    og = steel_background((1200, 630))
    logo_og = resize(logo_rgba, 680)
    ox = (1200 - logo_og.size[0]) // 2
    oy = (630 - 6 - logo_og.size[1]) // 2
    og_rgba = og.convert("RGBA")
    og_rgba.alpha_composite(logo_og.convert("RGBA"), (ox, oy))
    og_rgba.convert("RGB").save(PUBLIC / "og.jpg", "JPEG", quality=84, optimize=True)

    noise = Image.effect_noise((180, 48), 48).convert("L").resize((180, 180), Image.Resampling.BILINEAR)
    grain = Image.new("RGBA", noise.size, (0, 0, 0, 0))
    src = noise.load()
    dst = grain.load()
    gw, gh = noise.size
    for y in range(gh):
        for x in range(gw):
            v = src[x, y]
            alpha = min(36, abs(v - 128) // 2)
            shade = 235 if v >= 128 else 0
            dst[x, y] = (shade, shade, shade, alpha)
    grain.save(TEXTURES / "grain.png", "PNG", optimize=True)

    print("logo", logo_web.size, (BRAND / "logo.webp").stat().st_size, "flat", logo_flat.size)
    print("mark", nav_mark.size)
    print("og", (PUBLIC / "og.jpg").stat().st_size)
    print("favicon", (PUBLIC / "favicon.ico").stat().st_size)
    print("crop", crop_box)


if __name__ == "__main__":
    main()
