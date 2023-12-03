const assert = require('node:assert');

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let idxLeft = 0;
  let idxRight = nums.length;

  while (idxRight - idxLeft > 1) {
    const midIndex = parseInt((idxRight - idxLeft) / 2) + idxLeft;
    const midNum = nums[midIndex];
    if (midNum === target) {
      return midIndex;
    }

    if (midNum > target) {
      idxRight = midIndex;
    } else if (midNum < target) {
      idxLeft = midIndex;
    }
  }
  return nums[0] === target ? 0 : -1;
};

assert.strictEqual(search([-1, 0, 3, 5, 9, 12], 9), 4);
assert.strictEqual(search([-1, 0, 3, 5, 9, 12], 2), -1);
