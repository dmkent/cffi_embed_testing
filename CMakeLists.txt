# CMakeLists files in this project can
# refer to the root source directory of the project as ${HELLO_SOURCE_DIR} and
# to the root binary directory of the project as ${HELLO_BINARY_DIR}.
cmake_minimum_required (VERSION 2.8.11)
project (cffi_embed)

##
## Set up the CFFI built extension
include(ExternalProject)
ExternalProject_Add(
    cffi_plugin_ext
    SOURCE_DIR ${cffi_embed_SOURCE_DIR}
    BUILD_COMMAND python <SOURCE_DIR>/_build.py
    INSTALL_DIR ${CMAKE_INSTALL_PREFIX}
    INSTALL_COMMAND mkdir -p <INSTALL_DIR>/lib
            COMMAND cp my_model.so <INSTALL_DIR>/lib/
            COMMAND mkdir -p <INSTALL_DIR>/include/
            COMMAND cp <SOURCE_DIR>/include/my_model.h <INSTALL_DIR>/include/
)
ExternalProject_Get_Property(cffi_plugin_ext INSTALL_DIR)
add_library(cffi_plugin SHARED IMPORTED)
set_property(TARGET cffi_plugin PROPERTY IMPORTED_LOCATION ${INSTALL_DIR}/lib/my_model.so)
add_dependencies(cffi_plugin cffi_plugin_ext)

include_directories(${INSTALL_DIR}/include)

add_subdirectory (c)
add_subdirectory (c++)
