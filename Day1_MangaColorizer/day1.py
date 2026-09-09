"""Inspect the input manga image before colorization."""

from pathlib import Path

from PIL import Image, UnidentifiedImageError


IMAGE_PATH = Path(__file__).with_name("manga.png")


def main() -> None:
    """Print basic metadata for the manga source image."""
    try:
        with Image.open(IMAGE_PATH) as img:
            print(f"Width and height: {img.size}")
            print(f"Image mode:       {img.mode}")
            print(f"Image format:     {img.format}")
    except FileNotFoundError:
        print(f"Image not found: {IMAGE_PATH}")
    except UnidentifiedImageError:
        print(f"Unsupported or invalid image: {IMAGE_PATH}")


if __name__ == "__main__":
    main()
