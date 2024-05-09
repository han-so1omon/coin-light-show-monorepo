mkdir -p ~/p/edgetpu
cd ~/p/edgetpu
wget https://github.com/feranick/gasket-driver/releases/download/v1.0-18.1/gasket-dkms_1.0-18_all.deb
sudo apt install linux-headers-generic dkms linux-headers-6.1.0-21-arm64 linux-headers-6.1.0-21-common linux-headers-arm64 linux-kbuild-6.1
sudo dpkg -i gasket-dkms_1.0-18_all.deb
wget https://github.com/feranick/libedgetpu/releases/download/16.0TF2.16.1-1/libedgetpu1-std_16.0tf2.16.1-1.bookworm_arm64.deb
sudo dpkg -i libedgetpu1-std_16.0tf2.16.1-1.bookworm_arm64.deb
wget https://github.com/feranick/TFlite-builds/releases/download/v.2.16.1/tflite_runtime-2.16.1-cp311-cp311-linux_aarch64.whl
sudo mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.bkp
sudo pip3 install --upgrade tflite_runtime-2.16.1-cp311-cp311-linux_aarch64.whl