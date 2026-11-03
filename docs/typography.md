# Typography

## Faces

| Role | Face | Weights | Why |
|---|---|---|---|
| Primary: headers, body, buttons, the wordmark | **Schibsted Grotesk** | 400 regular, 600 semibold, 700 bold, 800 extrabold (variable, 400–900) | A grotesk with sturdy, slightly squared counters that hold up at 13px and turn assertive at 800. Its round `o` and `w` echo the disc and ring. |
| Secondary: account tails, addresses, CIDs | **JetBrains Mono** | 400 regular | Every account on Follows is a long base32 string. A monospace face with distinct `0`/`o`, `1`/`l` and `5`/`s` lets people compare them by eye. |

Both are under the SIL Open Font License and are self-hosted as WOFF2: [`fonts/`](../fonts) holds the files, with [`tokens.css`](../tokens.css) declaring them. Never load either from a font CDN.

`fonts/` also holds Schibsted Grotesk's `latin-ext` subset. Serve both with a `unicode-range`, as the Follows app does, so a page loads the extended set only for names that need it.

## Web-safe fallbacks

```css
--font-sans: "Schibsted Grotesk", system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
--font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
```

Load with `font-display: swap`. The fallbacks are the platform UI faces, which are close in width; the layout should not jump more than a few pixels when the brand faces arrive.

## Scale

| Style | Face | Size / line height | Weight | Case | Use |
|---|---|---|---|---|---|
| `display` | Sans | 32 / 1.15 (26 under 520px) | 700 | Sentence case | One per page: the home headline. |
| `title` | Sans | 26 / 1.2 | 700 | As written (`@ada`, `…ada4`) | A person's page. |
| `heading` | Sans | 22 / 1.25 | 700 | Sentence case | A list's title: "Followers of @ada". |
| `wordmark` | Sans | 19 / 1.2 | 800 | Title case: "Follows" | The name as live text in a header. Elsewhere use the outlined wordmark. |
| `body` | Sans | 16 / 1.45 | 400 | Sentence case | All running text. |
| `button` | Sans | 16 / 1.25 | 600 | Sentence case | Buttons and active tabs. |
| `label` | Sans | 15 / 1.35 | 700, in `muted` | Sentence case | Section labels. |
| `small` | Sans | 14 / 1.4 | 400 | Sentence case | Counts, secondary links. |
| `caption` | Sans | 13.6 / 1.35 | 400, in `muted` | Sentence case | Notes under buttons, captions. The smallest size used. |
| `address` | Mono | 14 / 1.4 | 400 | Lowercase, as the chain writes it | Account tails, addresses, CIDs. |

## Graphics and slides

- Headlines in Schibsted Grotesk 800 at 40px or more, tracked −1%, sentence case. 700 below 40px.
- Supporting lines in 400 at no less than half the headline size.
- Numbers in big figures use 700 with tabular figures (`font-variant-numeric: tabular-nums`).
- An address or CID in a graphic is JetBrains Mono, shortened to its tail with a leading ellipsis (`…ada4`) unless the whole string is the point.

## Case

- **Sentence case** for everything: headings, buttons, labels, menu items, slide titles. "Recently viewed", not "Recently Viewed".
- **Title case** only for proper names: Follows, Lattice, Selfhold, Moniker, Stoa, Murmur.
- **No all caps.** Follows has no uppercase labels or eyebrows. Emphasis comes from weight and color.
- **Handles** are lowercase with `@`; **account tails** lowercase with `…`.

## Rules

- Keep running text to about 65 characters a line.
- Use weight for hierarchy, never italics: Schibsted Grotesk ships no italic here, and a synthesized slant looks broken.
- Turn on `tabular-nums` wherever numbers stack in columns or update in place (follower counts).
- Headings take `text-wrap: balance`.
- Nothing below 13.6px on screen.
