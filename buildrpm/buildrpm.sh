#! /bin/bash
flume_url="https://downloads.apache.org/flume/1.9.0/apache-flume-1.9.0-bin.tar.gz"
flume_tar='apache-flume-1.9.0-bin.tar.gz'
tar_path="rpmbuild/SOURCES/$flume_tar"
mkdir -pv rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES}
if [ ! -f "$tar_path" ]; then
echo "download $flume_tar , It may take a long time!"
wget -O $tar_path $flume_url
else
echo "$flume_tar has exists!"
fi
rpmbuild -D "_topdir `pwd`/rpmbuild" -bb rpmbuild/SPECS/flume.spec
#rm -rf rpmbuild/SOURCES/*
