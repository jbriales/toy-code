#include <array>
#include <iostream>

struct Agg {
  std::string a;
  std::string b;
};

int main(int argc, char *argv[]) {
  Agg foo{"a", "b"};

  std::array<int, 4> arr_of_int = {1, 2, 3, 4};
  //  std::array<Agg, 4> arr_of_agg = {{"a", "b"}, {"a", "b"}, {"a", "b"}, {"a",
  //  "b"}}; // Does not compile!
  std::array<Agg, 4> arr_of_agg = {"a", "b", "a", "b",
                                   "a", "b", "a", "b"}; // Compiles!

  std::cout << "Done right!" << std::endl;
  return 0;
}
