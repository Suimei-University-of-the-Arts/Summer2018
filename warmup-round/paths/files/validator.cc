#include "testlib.h"

#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

int main(int argc, char** argv) {
  registerValidation(argc, argv);
  int n = inf.readInt(1, 300000, "N");
  inf.readSpace();
  int m = inf.readInt(1, 300000, "M");
  inf.readSpace();
  int k = inf.readInt(1, 5, "K");
  inf.readEoln();
  for (int i = 0; i < n; ++i) {
    if (i) inf.readSpace();
    inf.readInt(1, k, "color");
  }
  inf.readEoln();
  std::set<std::pair<int, int>> edges;
  for (int i = 0; i < m; ++i) {
    int a = inf.readInt(1, n, "a");
    inf.readSpace();
    int b = inf.readInt(1, n, "b");
    inf.readEoln();
    ensuref(a != b, "a != b");
    if (a > b) std::swap(a, b);
    edges.emplace(a, b);
  }
  ensuref(edges.size() == m, "no multiple edges");
  inf.readEof();
  return 0;
}