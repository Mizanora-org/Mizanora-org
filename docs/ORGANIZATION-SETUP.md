# Publish the Mizanora organization showcase

GitHub displays an organization's public profile from a specially named **`.github` repository owned by that organization**, not from a repository named after the organization.

This checkout is `muaaziqbalvip/Mizanora-org`. Its README works here immediately, but does not automatically change `github.com/Mizanora-org`.

## Organization homepage installation

1. Create or open the public repository **`Mizanora-org/.github`**. Organization write permissions are required.
2. Copy this repository's **`profile/README.md`** into that repository as **`profile/README.md`**.
3. Copy this repository's **`profile/assets/` directory** into that repository as **`profile/assets/`**. The README uses relative asset paths, so keep this layout:

   ```text
   .github/
   └── profile/
       ├── README.md
       └── assets/
           ├── hero.svg
           ├── ecosystem.svg
           ├── principles.svg
           └── footer.svg
   ```

4. Save the files on the target repository's default branch, then visit <https://github.com/Mizanora-org> while signed out to verify the public profile.

No scheduled workflow, API token or animation service is needed. Badges are optional and use Shields.io.

## Maintain this version

- Edit `README.md` for the copy and links.
- Run `python3 scripts/build-art.py` to regenerate local SVG artwork.
- Run `cp README.md profile/README.md` to synchronize the organization-ready README.
- Recopy the updated README and artwork to the organization `.github` repository when publishing changes.

Animation is embedded CSS inside SVG images. Rendering depends on the viewer; all banners have readable static content and a reduced-motion mode. GitHub README HTML cannot run arbitrary JavaScript or host interactive UI.
