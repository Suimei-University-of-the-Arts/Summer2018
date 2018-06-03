#include "testlib.h"

#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

int main(int argc, char** argv) {
  registerValidation(argc, argv);
  int n = inf.readInt(1, 9, "n");
  inf.readEoln();
  for (int i = 0; i < n; ++i) {
    inf.readToken("[a-z]{1-10}", "s");
		inf.readEoln();
	}
  inf.readEof();
  return 0;
}