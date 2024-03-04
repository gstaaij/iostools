#!/bin/bash

set -e

echo "[*] Welcome to basti564's automatic fakesigner"
echo "[*] Modified by gstaaij"
echo ""
if [[ $EUID -eq 0 ]]; then
    echo "[!] Please don't run this script as root!"
    exit 1
fi

if command -v ldid > /dev/null; then
    echo "[§] Found ldid"
else
    echo "[!] ldid not found!"
    echo "[!] Please install ldid"
    echo "[!] Refer to README.md for more details"
    exit 1
fi

if [ -z "$1" ]; then
    echo "[!] No .ipa file supplied!"
    exit 1
fi

ipa=$1
echo "[*] Unpacking.."
cd "$(dirname '$ipa')"
unzip "$ipa" > /dev/null
cd Payload
app=$(ls -1)
echo "[*] Fakesigning \"${app:0:${#app}-4}\""
ldid -S "$app/${app:0:${#app}-4}"
echo "[*] Fakesigning all Frameworks.."
if [ -d "$app/Frameworks" ]; then
    for f in "$app"/Frameworks/*.dylib; do
        echo "[*] Fakesigning \"$f\""
        ldid -S "$f"
    done
else
    echo "[*] No Frameworks found"
fi
cd ..
echo "[*] Packaging.."
zip -r "${ipa}-fakesigned.ipa" Payload > /dev/null
rm -f -r Payload
echo ""
echo "[*] Created ${ipa}-fakesigned.ipa"
