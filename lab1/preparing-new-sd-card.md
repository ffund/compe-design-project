---
title: Preparing a new micro SD card
---

All students in the ECE-UY 4313 lab are given a micro SD card at the beginning of the semester. The micro SD card is prepared with a Raspberry Pi OS "disk image" that you can boot on a Raspberry Pi Zero W. It is also pre-configured to enable SSH and to connect to the `ece4313` network in the lab the first time it boots.

However, if at any point in the year your micro SD card becomes corrupted, you will have to write a new "disk image" to it by yourself. Your micro SD card may become corrupted if you disconnect your Pi from the power supply without a "graceful" shutdown, or if the external circuit connected to your Pi causes it to shut down suddently.

This document describes the steps you would take to prepare a new micro SD card. But, be aware that this procedure will:

* take a while, and
* erase **everything** on your Pi's SD card, including any software libraries you have installed previously (they will need to be re-installed) and any configuration changes you have made (such as enabling various communication peripherals, changing your password, or configuring the Pi to connect to your home network).

You should only attempt this if your existing card becomes unusable, and the instructor has advised that you will need to prepare your SD card again.

# Procedure for preparing a new micro SD card

## Write a disk image with Etcher

To prepare the micro SD card for use, we will use a free application called [Etcher](https://www.balena.io/etcher/). Download Etcher onto your laptop: [`https://www.balena.io/etcher/`](https://www.balena.io/etcher/)

You will also need to download the Raspberry Pi OS image from [https://www.raspberrypi.org/software/operating-systems/](https://www.raspberrypi.org/software/operating-systems/). Several versions are available on that page; we are using the "Raspberry Pi OS with desktop and recommended software" version with release date May 7th 2021.

To use Etcher to write an image to a micro SD card:

* Open Etcher.
* Click \keys{Select Image}
* Navigate to the download location.
* Select the image file e.g. `2021-05-07-raspios-buster-armhf-full.zip`.
* Insert your micro SD card into a USB-micro SD adapter, then plug it into your computer's USB port.
* Click \keys{Select Target}, and make sure that Etcher has found the micro SD card to write to. (To be safe, you may want to make sure any other USB flash drives or portable drives are physically disconnected from your computer, so you can't accidentally overwrite them.)
* Click \keys{Flash}.
* When it's finished, you can close Etcher. 

## Additional configuration for headless use


Before you can use this SD card in a Raspberry Pi, you will need to configure it to

* enable SSH, and
* connect to the `ece4313` network (and/or any other network that you need your Pi to connect to)

**Note**: These instructions assume that you have a terminal running a `bash`, `zsh`, or similar shell. If you are using Linux or Mac, your operating system has a built-in terminal running `bash` or `zsh`.  If you are Windows, you can use the [Git Bash](https://git-scm.com/downloads) terminal.

Open a terminal, and navigate to the SD card filesystem named `boot`. At the terminal prompt, inside this filesystem, run:

```
touch ssh
```

to create a blank file called `ssh` inside the `boot` directory. This will enable SSH when the Pi boots for the first time, so that you will be able to connect to it in "headless" mode (without having to attach a monitor and/or keyboard).

Also, in your terminal, run

```
nano wpa_supplicant.conf
```

to create a new WiFi configuration file using `nano`.

Put the [following contents](wpa_supplicant.conf) (exactly!) in the file.

```
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="ece4313"
    psk="CompEDP1"
}
```

To save (write **o**ut) the file, use \keys{Ctrl+O}, and hit \keys{Enter} when prompted (at the bottom) to accept the file name. Look for a message indicating "Wrote 8 lines" (or similar). Then, quit `nano` with \keys{Ctrl+X}.

Make sure that the files have been created: run

```
ls
```

and check that both files (`ssh` and `wpa_supplicant.conf`) appear. Also check the file contents by running

```
cat ssh
```

(this file should be blank), and

```
cat wpa_supplicant.conf
```

(this file should be exactly as shown above.)

Once you have completed this configuration, you can remove the micro SD card from the USB adapter, and use it with your Pi. Your Pi will be configured to accept logins over SSH, and to connect to the WiFi network in the lab (`ece4313`).