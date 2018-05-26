#include "testlib.h"

#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

int main(int argc, char** argv) {
  registerValidation(argc, argv);
  int n = inf.readInt(3, 4100, "N");
  inf.readSpace();
  int m = inf.readInt(3, 4100, "M");
  inf.readSpace();
  int k = inf.readInt(1, m, "K");
  inf.readEoln();
  for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			char ch = inf.readChar();
			ensuref(ch == 'A' || ch == 'C' || ch == 'G' || ch == 'T', "ACGT");
		}
		inf.readEoln();
	}
  inf.readEof();
  return 0;
}