# Quit Smoking Tools

This repository contains a small progressive web app for tracking days since quitting
smoking (`index.html`) as well as related assets. A new script `parse_flyer.py`
can be used to extract visible text from an HTML file, which is useful for
converting a store's web flyer to plain text.

## Extract text from a web flyer

Save the flyer page as an HTML file (for example `flyer.html`) and run:

```bash
python3 parse_flyer.py flyer.html > flyer.txt
```

The script strips text inside `<script>` and `<style>` tags and prints the
remaining visible text. You can then search the output for special sale items.
