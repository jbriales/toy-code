#include "foo.h"

#include <iostream>

#include "global.h"

void CoutGlobal() {
  std::cout << "GetGlobalVarRef() inside foo.cpp: " << GetGlobalVarRef()
            << std::endl;
}
