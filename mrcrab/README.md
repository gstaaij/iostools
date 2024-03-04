
# Patching the Mr. Crab savefile

This is for educational purposes only.
I am not responsible for any damage to you or your iDevice.

## Prerequisites

- An iPhone or iPad that is jailbroken
  - For the `scp` method of obtaining `registry.db`, you also need to install OpenSSH on your iDevice.
- An ipa file for Mr. Crab 1.2.0 or above
  - (1.1.2 and earlier don't need patching, because all the levels are free in those versions, and there are no crab "costumes" yet)
- A computer that has Python installed
- For the `scp` command: some sort of ssh client

## Instructions

First, retrieve `registry.db` from your iDevice.
You can do this however you like, but if you have OpenSSH installed, you can do it with the following command.

You can use [SSH over USB](https://iphonedev.wiki/SSH_Over_USB) if you like.

You need to replace `<ip>` with the IP address of your iDevice.
You can find this by going to the WiFi settings and pressing the `i` button next to the network you're connected to.
You can also use [SSH over USB](https://iphonedev.wiki/SSH_Over_USB) if you like.

You also need to replace `<UUID>` with the UUID of Mr. Crab.
To get the UUID, please refer to the command at the bottom.

The default password is `alpine`.

```console
$ scp -o HostKeyAlgorithms=+ssh-rsa mobile@<ip>:/private/var/mobile/Containers/Data/Application/<UUID>/Library/Documents/registry.db .
```

Now, make a backup of `registry.db`, just in case:

```console
$ cp registry.db registry.db.bak
```

Run the patcher script:

```console
$ python ./patch.py
```

And finally copy `registry.db` back to the iDevice.

```console
$ scp -o HostKeyAlgorithms=+ssh-rsa ./registry.db mobile@<ip>:/private/var/mobile/Containers/Data/Application/<UUID>/Library/Documents/registry.db
```

### Getting the UUID

SSH into your iDevice and run the following commands:

```console
$ cd /private/var/mobile/Containers/Data/Application
$ echo */Library/Documents/registry.db
```
