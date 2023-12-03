/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const pairSumOrLess = (nums, target) => {
  const sortedNums = [...nums].sort((a, b) => a - b);

  let l = 0;
  let r = sortedNums.length - 1;
  let max = 0;
  let result = [-1, -1];

  while (l < r) {
    const num1 = sortedNums[l];
    const num2 = sortedNums[r];
    const sum = num1 + num2;
    if (sum <= target) {
      if (sum > max) {
        max = sum;
        result = [num1, num2];
      }
      l++;
    } else {
      r--;
    }
  }

  return result;
};

console.log(pairSumOrLess([6, 4, 2, 3, 8], 13));
