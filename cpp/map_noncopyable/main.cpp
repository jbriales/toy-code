#include <iostream>
#include <map>

namespace NonCopyable_NoNonconstCopyConstr {
struct Foo {
  // Constructor needs to be explicitly defaulted due to copy-constr delete
  Foo() = default;

  Foo(Foo &) = delete;
};
using NonCopyable_NoNonconstCopyConstr = Foo;

void test() {
  // Can be normally constructed (default constructor)
  NonCopyable_NoNonconstCopyConstr foo;
  // Cannot be used within pair
  std::pair<int, NonCopyable_NoNonconstCopyConstr> pair; // won't compile

  // However, the issue with lack of move-constructor above
  // can be circumvented with a piecewise_construct scheme
  // NOT WORKING
  //  std::pair<int, NonCopyable_NoNonconstCopyConstr> pair_nondefault{
  //      std::piecewise_construct, std::forward_as_tuple(1),
  //      std::forward_as_tuple()};

  // The trick above also allows to insert elements in a map
  // NOT WORKING
  //  std::map<int, NonCopyable_NoNonconstCopyConstr> map;
  //  map.emplace(std::piecewise_construct, std::forward_as_tuple(1),
  //              std::forward_as_tuple());
}
} // namespace NonCopyable_NoNonconstCopyConstr

namespace NonCopyable_NoConstCopyConstr {
struct Foo {
  // Constructor needs to be explicitly defaulted due to copy-constr delete
  Foo() = default;

  Foo(const Foo &) = delete;
};
using NonCopyable_NoConstCopyConstr = Foo;

void test() {
  // Can be normally constructed (default constructor)
  NonCopyable_NoConstCopyConstr foo;
  // Can be used within pair
  std::pair<int, NonCopyable_NoConstCopyConstr> pair_default;
  // Cannot be used with explicit constructor
  //  std::pair<int, NonCopyable_NoConstCopyConstr> pair_nondefault{
  //      1, NonCopyable_NoConstCopyConstr()}; // won't compile

  // However, the issue with lack of move-constructor above
  // can be circumvented with a piecewise_construct scheme
  std::pair<int, NonCopyable_NoConstCopyConstr> pair_nondefault{
      std::piecewise_construct, std::forward_as_tuple(1),
      std::forward_as_tuple()};

  // The trick above also allows to insert elements in a map
  std::map<int, NonCopyable_NoConstCopyConstr> map;
  map.emplace(std::piecewise_construct, std::forward_as_tuple(1),
              std::forward_as_tuple());
}
} // namespace NonCopyable_NoConstCopyConstr

namespace NonCopyableButMovable {
struct Foo {
  // Constructor needs to be explicitly defaulted due to copy-constr delete
  Foo() = default;

  Foo(const Foo &) = delete;

  Foo(Foo &&) = default;
};
using NonCopyableButMovable = Foo;

void test() {
  // Can be normally constructed (default constructor)
  NonCopyableButMovable foo;
  // Can be used within pair
  std::pair<int, NonCopyableButMovable> pair_default;
  // Can be used with explicit constructor
  std::pair<int, NonCopyableButMovable> pair_nondefault{
      1, NonCopyableButMovable()};
}
} // namespace NonCopyableButMovable

struct A {
  A() {}
  //  A(A &) = delete;
  //  A(const A &) = delete;

  // NOTE: If const constr is not deleted, there will be issues with std::pair
  // TODO: Swap comments to see error
  A(const A &) = delete;
  //  A(A &) = delete;
};

struct B {
  B(int a) {}

  B(const B &) = delete;
  //  B(B &) = delete;

  B(B &&) = default;
};

int main() {
  NonCopyable_NoNonconstCopyConstr::test();

  // A pair can be created with default constructor
  std::pair<int, A> p1;
  // If a non-default constructor is needed, the above won't work
  // E.g.
  // std::pair<int, B> pB;  // will fail to compile

  std::pair<int, B> p2{1, B(2)};

  //  std::map<int, A> map;
  //  map.insert(std::make_pair(1, A()));
  //  map.emplace(1, A());

  return 0;
}

class SizeT {
public:
  // implicit conversion
  operator size_t() const { return val_; }

protected:
  explicit SizeT(size_t val) : val_(val) {}

private:
  size_t val_;
};

class ImuId : public SizeT {
public:
  explicit ImuId(size_t val) : SizeT(val) {}
};

// non-copyable but movable
struct non_copyable {
  non_copyable() = default;

  non_copyable(non_copyable &&) = default;
  non_copyable &operator=(non_copyable &&) = default;

  // you shall not copy
  non_copyable(const non_copyable &) = delete;
  non_copyable &operator=(const non_copyable &) = delete;
};

class NoncopyableFoo {
public:
  NoncopyableFoo() {}
  NoncopyableFoo(int a) {}

  NoncopyableFoo(NoncopyableFoo &&) = default;

  NoncopyableFoo(const NoncopyableFoo &) = delete; // non construction-copyable
  NoncopyableFoo &operator=(const NoncopyableFoo &) = delete; // non copyable
};

int main(int argc, char *argv[]) {

  NoncopyableFoo a_foo{1};

  // Typical map
  std::map<int, int> a_map;
  a_map.insert({1, 2});

  // A map with non-copyable member
  std::map<int, NoncopyableFoo> a_map_with_noncopyable_values;
  //  a_map_with_noncopyable_values.insert({1, NoncopyableFoo{2}});
  a_map_with_noncopyable_values.insert(std::make_pair(1, NoncopyableFoo{2}));

  //  typedef std::map<int, NoncopyableFoo> map_type;
  //  a_map_with_noncopyable_values.insert(
  //      (map_type::value_type({1, NoncopyableFoo()})));

  std::map<SizeT, non_copyable> map;
  // map.insert({ 1, non_copyable() });  < FAILS
  map.insert(std::make_pair(ImuId(1), non_copyable{}));
  // ^ same and works

  return 0;
}
