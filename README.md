
# Tiny Synology DiskStation daemon

This very basic service was created for a Synology DiskStation DS214+ running
Debian (Bookworm). It should also work on other Synology NAS products like the
DS414 or the DS207.

The daemon will turn off the blinking LED at startup and shut the system down
when the power button is pressed.

Installation:
```
git clone https://github.com/easybe/synd.git /usr/local/synd
pip3 install -r /usr/local/synd/requirements.txt
systemctl enable /usr/local/synd/synd.service
systemctl start synd
```

In order for the device to actually power off, we need to enable the
`qnap-poweroff` driver. Also, to preserve the MAC addresses set by U-Boot, the
`mvneta` driver must be compiled into the kernel.

The Linux kernel I cross-compile as follows using
[a Docker image](https://hub.docker.com/r/easybe/debian-armhf-build):
```
apt source linux
cd linux-*
cp /path/to/old/config .config
sed -i 's/CONFIG_MVNETA=m/CONFIG_MVNETA=y/' .config
sed -i 's/.*CONFIG_POWER_RESET_QNAP.*/CONFIG_POWER_RESET_QNAP=y/' .config
sed -i 's/CONFIG_SYSTEM_TRUSTED_KEYS=.*/CONFIG_SYSTEM_TRUSTED_KEYS=""/' .config
export ARCH=arm
export CROSS_COMPILE=arm-linux-gnueabihf-
export LOCALVERSION=-armmp-lpae
export KDEB_PKGVERSION=$(make kernelversion)-1+custom
make oldconfig
make -j $(nproc) bindeb-pkg
```
