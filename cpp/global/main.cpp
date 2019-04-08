#include <iostream>

#include "foo.h"

#include "global.h"

int main(int argc, char *argv[]) {
  std::cout << "Hello World!" << std::endl;

  std::string &global_var = GetGlobalVarRef();
  std::cout << "global_var: " << global_var << std::endl;

  global_var = "foo-string";
  CoutGlobal();

  return 0;
}
