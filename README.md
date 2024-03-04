
# gstaaij's iOS Tools

These are a few useful tools I made or modified.

## Included tools

- A modified version of [fakesigner](https://github.com/basti564/fakesigner)
  - It works when there are spaces in the path of the .ipa
  - It doesn't spit out every file it's extracting and rearchiving to stdout
  - It doesn't require Homebrew for it to work at all
- A savefile patcher for Mr. Crab
  - Unlocks all levels and costumes
- sinfstripper
  - Removes `SC_Info/${appName}.sinf` from an .ipa file because that file reveals the Apple ID of the person who purchased the app
  - Based on fakesigner

## Other useful tools

- [frida-ios-dump](https://github.com/AloneMonkey/frida-ios-dump)
- [bagbak](https://github.com/ChiChou/bagbak)
  - Only use this one if you don't intend to install the .ipa to an iDevice, because you can't. You could use this if the app you're trying to dump isn't opening, because — unlike frida-ios-dump — it doesn't need to open the app to dump it.