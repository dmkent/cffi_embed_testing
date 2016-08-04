add_executable (testcpp test.cpp)

SET(CMAKE_CXX_FLAGS "-std=c++11")
target_link_libraries (testcpp cffi_plugin)

INSTALL(TARGETS testcpp 
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
)

