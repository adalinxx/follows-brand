#!/bin/sh
# Renders the PNG icons from their SVGs at their own size, in headless Chrome.
#   sh source/png.sh <out>
set -eu
OUT=${1:-.}
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
render() { # svg size png
  printf '<html><body style="margin:0;background:transparent"><img src="%s" width="%s" height="%s" style="display:block"></body></html>' "file://$OUT/$1" "$2" "$2" > "$OUT/.render.html"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --default-background-color=00000000 --screenshot="$OUT/$3" --window-size="$2,$2" "file://$OUT/.render.html" 2>/dev/null
}
render favicons/favicon-tile-16.svg 16 favicons/favicon-16.png
render favicons/favicon-tile-32.svg 32 favicons/favicon-32.png
render favicons/app-icon.svg 180 favicons/apple-touch-icon.png
render favicons/app-icon.svg 512 favicons/icon-512.png
rm -f "$OUT/.render.html"
