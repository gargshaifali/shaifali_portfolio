# Shaifali Garg — Portfolio

A clean, responsive single-page portfolio website (gradient hero + light body).
Built with plain HTML, CSS, and vanilla JavaScript — zero build step, zero dependencies.

## Structure

```
.
├── index.html          # All page content / sections
├── css/styles.css      # Styling & responsive layout
├── js/main.js          # Nav, typewriter, mobile menu, scroll reveal
└── assets/
    └── Shaifali_Garg_Resume.pdf
```

## Run locally

Just open `index.html` in a browser, or serve it:

```bash
python -m http.server 8000
# then visit http://localhost:8000
```

## Deploy to Walmart Enterprise GitHub Pages

1. Create a repo on https://gecgithub01.walmart.com/s0g0em7
   (e.g. `s0g0em7.github.io` for a user site, or any repo name for a project site).
2. Push this folder's contents to the repo (see commands below).
3. In the repo **Settings → Pages**, set the source to the `main` branch, root folder.
4. Your site will be served from the URL shown on that Pages settings screen.

```bash
git remote add origin https://gecgithub01.walmart.com/s0g0em7/<repo-name>.git
git branch -M main
git push -u origin main
```

## Editing content

All text lives in `index.html`. The rotating job titles in the hero are in
`js/main.js` (the `roles` array). Colors/theme tokens are at the top of
`css/styles.css` under `:root`.
