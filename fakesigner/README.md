
# fakesigner

Automatically fakesign any .ipa file for use with [AppSync Unified](https://cydia.akemi.ai/?page/net.angelxwind.appsyncunified) or similar

## Usage

Run ```path/to/fakesigner.sh path/to/app.ipa``` and the script will automatically create a fakesigned .ipa file ```path/to/app.ipa-fakesigned.ipa```

## Dependencies

- `ldid` from your package manager of choice
  - [AUR](https://aur.archlinux.org/packages/ldid) or [the git version](https://aur.archlinux.org/packages/ldid-git) (both are the Procursus fork)
  - [Homebrew](https://formulae.brew.sh/formula/ldid) or [the Procursus fork](https://formulae.brew.sh/formula/ldid-procursus)
  - Alternatively, you can build `ldid` from source and add it to your PATH
