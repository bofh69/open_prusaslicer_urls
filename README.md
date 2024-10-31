# Open PrusaSlicer URLs
A simple script to download files from prusaslicer urls and then open
them with OrcaSlicer (or another program with a simple edit).

This has only been tested with a rather vanilla Ubuntu 22.04 and Firefox.

## How to install

Run:
```sh
cp open_prusaslicer_urls.desktop ~/.local/share/applications/
sed -i -e "s:PATH:$(pwd):" ~/.local/share/applications/open_prusaslicer_urls.desktop
xdg-mime default open_prusaslicer_urls.desktop x-scheme-handler/prusaslicer
update-desktop-database ~/.local/share/applications/
```

You might need to edit `open_prusaslicer_urls.py` and replace `OrcaSlicer`
with another program name, or the full path to the slicer.

## How to use

When pressing a "Slice" button on printables.com, the browser might
ask which program to use to open it. Choose "System Handler".
