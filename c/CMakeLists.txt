add_executable (test test.c)

target_link_libraries (test cffi_plugin)

INSTALL(TARGETS test
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
)

