#!/bin/bash

set -e

echo "Welcome to gstaaij's automatic sinfstripper"
echo -e "Copyright \u00a9 gstaaij. Licensed under MIT."
echo ""

if [[ $EUID -eq 0 ]]; then
    echo "Please don't run this script as root!"
    exit 1
fi

if [ -z "$1" ]; then
    echo "No .ipa file supplied!"
    exit 1
fi

ipa=$1
echo "Unpacking..."
cd "$(dirname '$ipa')"
unzip "$ipa" > /dev/null
cd Payload
app=$(ls -1)
echo "Removing \"SC_Info/${app:0:${#app}-4}.sinf\""
rm "$app/SC_Info/${app:0:${#app}-4}.sinf"
cd ..
echo "Packaging..."
zip -r "${ipa}_sinfstripped.ipa" Payload > /dev/null
rm -f -r Payload
echo ""
echo "Created \"${ipa}_sinfstripped.ipa\""
