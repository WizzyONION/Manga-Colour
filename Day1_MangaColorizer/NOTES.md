# Day 1: Convert Manga to RGB

## What this step does

`convert_manga_to_rgb.py` opens `manga.png`, converts it to RGB mode, and saves the result as `output/manga_rgb.png`.

RGB means every pixel has three colour channels:

- **R** — red
- **G** — green
- **B** — blue

Using RGB gives later colourization steps a predictable image format. It also removes transparency information if the original image uses an alpha channel, such as `RGBA`.

## Run the script

From the repository root:

```bash
.venv/bin/python Day1_MangaColorizer/convert_manga_to_rgb.py
```

If you have not created the local environment yet:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install Pillow
.venv/bin/python Day1_MangaColorizer/convert_manga_to_rgb.py
```

## Expected result

The terminal prints the original image mode, confirms the new RGB mode, and gives the full output path. The generated file appears here:

```text
Day1_MangaColorizer/output/manga_rgb.png
```

## Why use `Path`?

The script builds file paths relative to its own location. This means it works whether you run it from the repository root or from another directory.

## Important note about RGB conversion

This conversion changes the **image format in memory**, not the look of a normal black-and-white manga page. It prepares the image for later processing, where colours can be added or predicted.
