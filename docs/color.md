# Color

One cool brand color, a family of blue-leaning neutrals, and one warm accent kept small. The neutrals carry a trace of Indigo's blue (CMYK shows it: cyan and magenta with no yellow), so grays sit with the brand rather than beside it.

## Primary

| Name | Token | HEX | RGB | CMYK | Use |
|---|---|---|---|---|---|
| Indigo | `accent` (light) | `#3346D3` | 51 70 211 | 76 67 0 17 | The brand. Follow button, links, focus, the mark's disc. |
| Indigo Deep | `accent-ink` (light) | `#1F2DA0` | 31 45 160 | 81 72 0 37 | Hover and pressed. |
| Periwinkle | `accent` (dark) | `#8D9BFF` | 141 155 255 | 45 39 0 0 | Indigo's place on dark grounds; the reversed mark's disc. |
| Periwinkle Light | `accent-ink` (dark) | `#B4BEFF` | 180 190 255 | 29 25 0 0 | Hover and pressed in dark; avatar initials. |

## Secondary: neutrals

| Name | Token | HEX | RGB | CMYK | Use |
|---|---|---|---|---|---|
| Ink | `ink` (light) | `#16181D` | 22 24 29 | 24 17 0 89 | Text, the wordmark, the mark's ring. |
| Slate | `muted` (light) | `#5F6470` | 95 100 112 | 15 11 0 56 | Secondary text. |
| Mist | `line` (light) | `#E6E7EB` | 230 231 235 | 2 2 0 8 | Hairlines. |
| Cloud | `soft` (light) | `#F4F5F7` | 244 245 247 | 1 1 0 3 | Fields, quiet panels. |
| Paper | `bg` (light) | `#FFFFFF` | 255 255 255 | 0 0 0 0 | Page ground. |
| Haze | `avatar` (light) | `#E3E6F8` | 227 230 248 | 8 7 0 3 | Avatar discs. |
| Night | `bg` (dark) | `#121418` | 18 20 24 | 25 17 0 91 | Dark page ground. |
| Graphite | `soft` (dark) | `#1C1F24` | 28 31 36 | 22 14 0 86 | Dark fields, panels. |
| Steel | `line` (dark) | `#2C2F36` | 44 47 54 | 19 13 0 79 | Dark hairlines. |
| Fog | `ink` (dark) | `#ECEDF0` | 236 237 240 | 2 1 0 6 | Dark-theme text; the reversed ring and wordmark. |
| Ash | `muted` (dark) | `#A3A8B3` | 163 168 179 | 9 6 0 30 | Dark-theme secondary text. |
| Dusk | `avatar` (dark) | `#262B45` | 38 43 69 | 45 38 0 73 | Dark avatar discs. |

## Accent

| Name | Token | HEX | RGB | CMYK | Use |
|---|---|---|---|---|---|
| Marigold | `highlight` | `#F5B335` | 245 179 53 | 0 27 78 4 | Small fills only: the "Follows you" chip, a new follower's dot. |
| Marigold Deep | `highlight-ink` (light) | `#8A5B00` | 138 91 0 | 0 34 100 46 | Marigold as text on light grounds. |

Proportion on a typical screen: about 90% neutrals, 8–10% Indigo, under 2% Marigold.

## Print

The CMYK values above are straight conversions from sRGB with no ICC profile. Use them as a starting point and proof on the actual stock: Indigo in particular is outside most CMYK gamuts and prints duller. For one-color jobs use the ink logo in black or the Indigo nearest to the press's spot color, matched by eye against a screen at `#3346D3`.

## Contrast and accessibility

WCAG 2.2 contrast ratios. AA asks 4.5:1 for body text and 3:1 for large text (24px, or 19px bold) and for icons, focus rings and control edges.

| Foreground | Background | Ratio | Passes for |
|---|---|---|---|
| Ink | Paper | 17.8 | All text, AAA |
| Ink | Cloud | 16.3 | All text, AAA |
| Slate | Paper | 5.9 | Body text, AA |
| Slate | Cloud | 5.4 | Body text, AA |
| Slate | Mist | 4.8 | Body text, AA (tight; avoid for small type) |
| Indigo | Paper | 7.1 | All text, AAA |
| Indigo | Cloud | 6.5 | Body text, AA |
| Indigo | Haze | 5.7 | Body text, AA (avatar initials) |
| Paper | Indigo | 7.1 | Button labels, AAA |
| Indigo Deep | Paper | 10.8 | All text, AAA |
| Fog | Night | 15.8 | All text, AAA |
| Fog | Graphite | 14.1 | All text, AAA |
| Ash | Night | 7.7 | All text, AAA |
| Ash | Graphite | 6.9 | Body text, AA |
| Periwinkle | Night | 7.3 | All text, AAA |
| Periwinkle | Graphite | 6.5 | Body text, AA |
| Night | Periwinkle | 7.3 | Button labels in dark, AAA |
| Periwinkle Light | Dusk | 7.8 | Avatar initials in dark, AAA |
| Ink | Marigold | 9.6 | Chip labels, AAA |
| Night | Marigold | 10.0 | Chip labels in dark, AAA |
| Marigold Deep | Paper | 5.9 | Body text, AA |

Pairs that fail, and are not allowed:

| Foreground | Background | Ratio | Instead |
|---|---|---|---|
| Indigo | Night | 2.6 | Periwinkle on Night (7.3) |
| Indigo | Ink | 2.5 | Fine inside the two-tone mark, where disc and ring are shapes, not text. Never Indigo text on Ink. |
| Periwinkle | Paper | 2.5 | Indigo on Paper (7.1) |
| Marigold | Paper | 1.85 | A Marigold fill with Ink text, or Marigold Deep text |
| Mist | Paper | 1.24 | Decorative hairlines only; a control's edge uses Slate (5.9) or relies on its fill |

Rules:
- **Focus:** a 2px solid `focus` ring, offset 2px, on every control: at least 6.5:1 on `bg` and `soft` in both themes.
- **Don't rely on color alone.** The Follow button changes its word ("Follow" to "Following") as well as its fill, and a chip carries its words ("Follows you"). A new follower's Marigold dot always comes with a count or label.
- **Dark theme isn't an inversion.** Indigo is swapped for Periwinkle, and button text turns dark (`on-accent`), because white on Periwinkle is only 2.5:1.

The values live in [`tokens.json`](../tokens.json); [`tokens.css`](../tokens.css) declares them as custom properties for both themes.
