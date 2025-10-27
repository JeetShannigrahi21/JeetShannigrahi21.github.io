# Personal Site

This repository contains the source for [https://jeetshannigrahi21.github.io](https://jeetshannigrahi21.github.io).

## Preview locally

```bash
python3 -m http.server 4000
```

Open <http://localhost:4000/> after running the server. Press `Ctrl+C` to stop it.

## Publish with GitHub Pages

1. Push the latest changes to the `main` branch.
2. In **Settings → Pages**, set **Source** to **Deploy from a branch**.
3. Choose the `main` branch and the `/ (root)` folder, then click **Save**.
4. Leave the **Custom domain** box empty if you want to use the default `jeetshannigrahi21.github.io` address.
5. Wait for the "GitHub Pages" deployment to finish (check the repository’s **Actions** tab). The site should then be available at the default URL.

If you set a custom domain, GitHub automatically creates a `CNAME` file in the repository and you must point your DNS records to GitHub Pages. Deleting or editing the `CNAME` file removes the custom domain.
