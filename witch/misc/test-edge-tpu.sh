cd ~/p
wget https://github.com/feranick/TFlite-builds/releases/download/v.2.16.1/test_edgetpu.tar.xz
tar xvaf test_edgetpu.tar.xz
cd test_edgetpu
python3 test_libedgetpu.py