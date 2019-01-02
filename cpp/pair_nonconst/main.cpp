#include <iostream>
#include <map>

namespace DeletedNonconstCopyConstr {
struct A {
  A() {}
  A(A &) = delete;
};

void test() {
  // Create a pair using default constructor
  std::pair<int, A> pair; // won't compile
}
} // namespace DeletedNonconstCopyConstr

namespace ExplicitNonconstCopyConstr {
struct A {
  A(A &) = default;
};

struct FooInherits : A {
  FooInherits(const FooInherits &) = default; // won't compile
};

struct FooContains {
  FooContains(const FooContains &) = default; // won't compile
  A a;
};

} // namespace ExplicitNonconstCopyConstr

int main() {
  DeletedNonconstCopyConstr::test();

  return 0;
}
