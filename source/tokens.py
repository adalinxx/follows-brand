# tokens.json -> tokens.css: custom properties for both themes, the font stacks and @font-face rules.
#   python3 source/tokens.py > tokens.css
import json, pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
t = json.loads((root / "tokens.json").read_text())
first, *rest = [th["id"] for th in t["color"]["themes"]]
alias = lambda v: re.sub(r"^\{(.+)\}$", r"var(--\1)", v)
val = lambda tok, theme: alias(tok["value"] if isinstance(tok["value"], str) else tok["value"].get(theme, tok["value"][first]))

out = ["/* Follows — generated from tokens.json by source/tokens.py */"]
for f in t["type"]["fonts"]:
    out.append(f'@font-face {{ font-family: "{f["family"]}"; font-weight: {f["weight"]}; font-style: {f.get("style", "normal")}; font-display: swap; src: url(./{f["file"]}) format("woff2"); }}')
out.append(":root {")
out += [f'  --{tok["name"]}: {val(tok, first)};' for tok in t["color"]["tokens"]]
out += [f'  --{tok["name"]}: {tok["value"]};' for fam in ("spacing", "radius", "size") for tok in t[fam]["tokens"]]
out += [f'  --font-{k}: {v};' for k, v in t["type"]["families"].items()]
out.append("}")
for theme in rest:
    block = [f'  --{tok["name"]}: {val(tok, theme)};' for tok in t["color"]["tokens"]
             if isinstance(tok["value"], dict) and tok["value"].get(theme) not in (None, tok["value"].get(first))] + ["  color-scheme: dark;"]
    out.append(f'@media (prefers-color-scheme: {theme}) {{ :root:not([data-theme="{first}"]) {{')
    out += ["  " + line for line in block]
    out.append("} }")
    out.append(f':root[data-theme="{theme}"] {{')
    out += block
    out.append("}")
for g in t["type"]["groups"]:
    for s in g["styles"]:
        fam = s.get("family", g["family"])
        rules = [f'font-family: var(--font-{fam})', f'font-size: {s["fontSize"]}', f'line-height: {s["lineHeight"]}', f'font-weight: {s["fontWeight"]}']
        if "letterSpacing" in s: rules.append(f'letter-spacing: {s["letterSpacing"]}')
        out.append(f'.{s["name"]} {{ {"; ".join(rules)}; }}')
print("\n".join(out))
