#!/bin/bash
# $Id$

# Use this script to (re)publish the documentation

export PROJECT="BcdaQWidgets"
export SOURCE_DIR="build"
export TARGET_DIR="/home/joule/SVN/subversion/bcdaext/ "
export MAKE_TARGET="all"
export MAKE_DIR="docs"
export PATH=/APSshare/epd/rh6-x86/bin/:$PATH

echo "Updating from subversion repository"
svn update

cd $MAKE_DIR

echo "rebuilding the documentation"
make clean
make $MAKE_TARGET

cd $SOURCE_DIR
echo "Removing the old build, if it exists"
/bin/rm -rf $PROJECT

echo "Copying the rebuilt web site"
mv html $PROJECT
tar cf - $PROJECT | ( cd $TARGET_DIR && tar xf - )
echo "Done publishing $PROJECT"
