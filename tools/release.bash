#!/usr/bin/env bash
#
# Create sdist release and upload to pypi. Also tag the current commit with the
# correct version number.
#
# Version number is taken from setup.cfg, so update accordingly.

CWD=$(cd $(dirname $0) ; pwd)

# Get the version number from setup.cfg.
version_num=$(cat $CWD/../setup.cfg | grep version | cut -d" " -f3)

if [ -z "${version_num}" ] ; then
    echo "[ERROR] Failed to find version number in setup.cfg."
    exit 1
fi
echo "Releasing version: ${version_num}"

echo "Moving to: ${CWD}/.."
cd $CWD/..

echo "Cleaning repo with git clean -dxf"
git clean -dxf

echo "Running python setup.py sdist upload ..."
PBR_VERSION=$version_num python setup.py sdist upload

echo "Tagging HEAD commit with ${version_num}."
git tag $version_num HEAD

echo "All done."
