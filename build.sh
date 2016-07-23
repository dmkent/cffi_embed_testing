#!/bin/bash

mkdir -p build

python _build.py
mv plugin.so my_model.o my_model.c build/

export CFLAGS="-Iinclude"
export CXXFLAGS="${CFLAGS} --std=c++11"

g++ ${CXXFLAGS} -o build/testcpp.o -c c++/test.cpp
g++ ${CXXFLAGS} -o testcpp -l:build/plugin.so build/testcpp.o

gcc ${CFLAGS} -o build/test.o -c c/test.c
gcc ${CFLAGS} -o test  -l:build/plugin.so build/test.o


PYTHONPATH=lib LD_LIBRARY_PATH=build ./test
PYTHONPATH=lib LD_LIBRARY_PATH=build ./testcpp
