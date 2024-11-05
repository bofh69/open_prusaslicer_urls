#!/usr/bin/env python3

""" Open prusaslicer links with OrcaSlicer. """

import os
import subprocess
import sys
import tempfile
import urllib.parse

import requests


# Parse:
# prusaslicer://open?file=https%3A%2F%2Ffiles.printables.com%2...filename.3mf

if len(sys.argv) < 2:
    raise RuntimeError("Missing argument")

if not sys.argv[1].startswith("prusaslicer://open?"):
    raise RuntimeError("Invalid argument", sys.argv[1])

ENCODED_URL = sys.argv[1][19:]
decoded_url = urllib.parse.parse_qs(ENCODED_URL)

file_url = decoded_url.get("file")
if not file_url:
    raise RuntimeError("No file argument in URL", decoded_url)
if len(file_url) != 1:
    raise RuntimeError("Wrong number of file arguments in URL", decoded_url)
file_url = file_url[0]

print(f"Downloading {file_url}")

suffix = ""  # pylint: disable=C0103
suffix_idx = file_url.rfind('.')
if suffix_idx:
    suffix = file_url[suffix_idx:]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://example.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}

response = requests.get(file_url, timeout=120, headers=headers)

if response.status_code != 200:
    raise RuntimeError(f"Failed to download file: {response.status_code} {response.content}")

with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
    temp_file.write(response.content)
    temp_file_name = temp_file.name

print(f"Stored in {temp_file_name}, now starting OrcaSlicer")

subprocess.run(["OrcaSlicer", temp_file_name], check=True)

os.remove(temp_file_name)
