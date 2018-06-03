#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

int main() {
  int n;
  std::cin >> n;
  std::vector<std::string> s(n);
  for (int i = 0; i < n; ++i) {
    std::cin >> s[i];
  }
  std::sort(s.begin(), s.end(), [](const std::string &x, const std::string &y){
    return x + y < y + x;
  });
  for (auto &&w: s) printf("%s", w.c_str());
  puts("");
  return 0;
}