// https://www.codewars.com/kata/55fd2d567d94ac3bc9000064

long long rowSumOddNumbers(unsigned n){
  unsigned firstTerm = (n*n) - (n - 1);
  long long netsum = 0;
  for (int i = 0; i < n; i++) {
      netsum = netsum + firstTerm;
      firstTerm += 2;
  }
  return netsum;
}

// REFACTORING
// Simply, the row sum is always n cubed.

long long rowSumOddNumbers(unsigned n){
  return n*n*n;
}
