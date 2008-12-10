#!/bin/sh
python setup.py install --root=package
rm -rf build
mkdir package/CONTROL
cp CONTROL/postinst CONTROL/postrm CONTROL/control package/CONTROL/
/usr/local/openmoko/arm/bin/ipkg-build -o root -g root package/
rm -rf package
