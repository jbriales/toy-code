/* This toy examples explores several features:
 * - Create timestamp for log file
 * - Basic logging to file using ofstream
 * - Create new folder for log
 */

#include <chrono>   // for time
#include <fstream>  // for ofstream
#include <iomanip>  // for std::put_time
#include <iostream> // for std::cout

#include <experimental/filesystem>
namespace fs = std::experimental::filesystem;

//#include <filesystem> // (since C++17)
// namespace fs = std::filesystem;

std::string GetTimestamp() {
  auto time_now =
      std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
  std::stringstream ss;
  ss << std::put_time(std::localtime(&time_now), "%F,%T");
  return ss.str();
}

std::ofstream OpenLogfilestream(const fs::path &path_logfile) {
  fs::path dirpath_log = path_logfile.parent_path();
  if (!fs::exists(dirpath_log)) {
    bool success = fs::create_directories(dirpath_log);
    if (!success) {
      std::cout << "Couldn't create dir" << std::endl;
    }
  }
  return std::ofstream{path_logfile, std::ofstream::out};
}

int main(int argc, char *argv[]) {
  std::cout << GetTimestamp() << std::endl;
  std::cout << "Current path: " << fs::current_path() << std::endl;

  fs::path path_logfile =
      fs::current_path() / ".log" / ("test_log," + GetTimestamp() + ".txt");
  std::ofstream ofs = OpenLogfilestream(path_logfile);
  ofs << "lorem ipsum";
  ofs.close();
  std::cout << "Log written to file " << path_logfile << std::endl;

  return 0;
}
