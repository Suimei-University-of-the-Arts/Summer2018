#include "testlib.h"
#include <vector>
#include <string>
#include <cstdio>

std::vector<std::string> tests = {
  "baabbabbbbabaabbbbbbbbabbabbbbbbaababbbbbbabbbbbbababbbbbbab",
  "babababbabbbbbbbbbbbbbbbbbbbbbbbbbabbabbabbbbbabbbbaaababaaa",
  "babaaababaaaaaaabaaabbaaabbaaaaaaaabbbaaaaaaabaaaaababaaaaaa",
  "abababbaabbaaaaabbbbbabababbaaabbaaaabababbbbbaabababaaaaabb",
  "abaabaabaaaaaaabaaabaabaaaaaaaaaaaaaaaaaaaaaaabbbaaaabaaaaba",
  "baaabaaababbaaaaabaaabaabaaaaabaababbaaaaabaaabbaaaaababbaba",
  "abaaaababaabaaabbbaaaaabaaaabaababbbabaabbaaabaaaaaaaabaabba",
  "ababa",
  "abbbbaababababbaaaaaabaaaabaaaaaabbaaaaabaaabaababababaabaab",
  "aabb",
  "babbbbbbbbbabbabbbbbbbabbbbbbbbbbbababbbabbbbabbbbbabbbbbbbb",
  "bbbbabaabaababaaaaabbbaabbbabbbbbbabbbbbabbabbbbbbbbaabbbbba",
  "aaaaaababaaaaababaaaaaaaaaaaaaaaaaaabaaaaaaabaaaaaaabaababaa",
  "babaaabaaaabbabbaabaabbaaaababbaabbabaababbaabbababaaaababaa",
  "aabbbbaabaaaaabaaaaaaaaaaaabbaaaaaaaaaabbabbaaaaaabaabaaaaaa",
  "aaababaaaaaaaaabaaaababaaaaaababaabaaaaaaaabaabaaaaaaaabaabb",
  "bbabbbbbbabbbbbbbbbbbabbbbabbbbaabbbbbababbbbbbbbabbbbabbaab",
  "bbababbbbbbbbbbbababbbbbbabbbbabbbbababbbbbabbbbbababbbbbbbb",
  "bababbbbaabbabbaaaabbabaaaabaabbabbabbabbabbbbbaabbbbbbaabbb",
  "bbbbaabbbbbbaababbbbabaabbabbaaabbabbbbbbbbabaaabbbbbbababbb"
};

int main(int argc, char** argv) {
  registerGen(argc, argv, 1);
  int cas = std::atoi(argv[1]);
  puts(tests[cas].c_str());
  return 0;
}