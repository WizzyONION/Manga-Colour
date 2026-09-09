"""Convert the manga source image to a standard RGB PNG."""

from pathlib import Path

from PIL import Image, UnidentifiedImageError


PROJECT_DIR = Path(__file__).resolve().parent
INPUT_PATH = PROJECT_DIR / "manga.png"
OUTPUT_PATH = PROJECT_DIR / "output" / "manga_rgb.png"


def main() -> None:
    """Convert manga.png to RGB and save it in the output directory."""
    try:
        OUTPUT_PATH.parent.mkdir(exist_ok=True)

        with Image.open(INPUT_PATH) as image:
            original_mode = image.mode
            rgb_image = image.convert("RGB")
            rgb_image.save(OUTPUT_PATH, format="PNG")

        print(f"Old mode: {original_mode}")
        print("New mode: RGB")
        print(f"Saved RGB image to: {OUTPUT_PATH}")
    except FileNotFoundError:
        print(f"Image not found: {INPUT_PATH}")
    except UnidentifiedImageError:
        print(f"Unsupported or invalid image: {INPUT_PATH}")


if __name__ == "__main__":
    main()
