# 1 Percent Club

One hub. Endless trading possibilities.

Static website: the main page (`index.html`) and the member desk (`account.html`). No build step.

## Publishing

`.github/workflows/pages.yml` publishes the site to GitHub Pages on every push to `main` (and hourly, to refresh the economic calendar).

1. **Settings → Pages → Build and deployment → Source:** choose **GitHub Actions**.
2. **Custom domain:** enter the domain and save. DNS at the registrar:

   | Type  | Name  | Value                     |
   |-------|-------|---------------------------|
   | A     | `@`   | `185.199.108.153`         |
   | A     | `@`   | `185.199.109.153`         |
   | A     | `@`   | `185.199.110.153`         |
   | A     | `@`   | `185.199.111.153`         |
   | CNAME | `www` | `alyph88fx-ops.github.io` |

3. When the DNS check passes, tick **Enforce HTTPS**.

Mock site: prices, charts, account data and forms are samples. Demo forms collect no payment details.
