#include "global.h"

#include <string>

std::string &GetGlobalVarRef() {
  static std::string *var = new std::string("");
  return *var;
}
