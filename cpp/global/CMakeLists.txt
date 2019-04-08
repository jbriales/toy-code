# Default project name based on folder
get_filename_component(FOLDER_NAME ${CMAKE_CURRENT_SOURCE_DIR} NAME)
string(REPLACE " " "_" FOLDER_NAME ${FOLDER_NAME})

project("toy_${FOLDER_NAME}")
cmake_minimum_required(VERSION 2.8)

add_executable(main "main.cpp" "global.cpp" "foo.cpp")
