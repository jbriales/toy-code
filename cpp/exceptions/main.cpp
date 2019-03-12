#include <exception>
#include <iostream>

class myexception : public std::exception {
  virtual const char *what() const throw() { return "My exception happened"; }
};

int main() {
  try {
    throw myexception{};
  } catch (std::exception &e) {
    std::cout << e.what() << '\n';
  }

  try {
    throw std::runtime_error{"A runtime error"};
  } catch (const std::runtime_error &e) {
    std::cout << e.what() << std::endl;
  }

  return 0;
}
