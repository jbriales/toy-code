#!/bin/bash

set -x
mkdir test
touch test/file1

cp -r ./test/* ./copy_of_file1
echo "There is one file in test/*, so it creates a copy of a file in the dst path"
tree

touch test/file2
cp -r ./test/* ./test-copy
echo "Fails because there are several files in test, but dst does not exist (it should be an existing folder)"

cp -r ./test ./test-copy
echo "Create copy directory of test"
tree

cp -r ./test ./test-copy
echo "Create copy directory of test, but test-copy exists, so it copies <src> inside"
tree

cp -r ./test ./intermediate/test-copy
echo "Copy src directory to a non-existing parent folder, it fails"
tree

rm -r test
rm -r test-copy
rm copy_of_file1
set +x
