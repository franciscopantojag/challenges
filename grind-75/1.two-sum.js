// https://leetcode.com/problems/two-sum/
const assert = require('node:assert');

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const twoSum = (nums, target) => {
  const dic = {};
  for (let i = 0; i < nums.length; i++) {
    const n = nums[i];
    const diff = target - n;

    if (diff in dic) {
      return [dic[diff], i];
    }

    dic[n] = i;
  }
};

assert.deepStrictEqual(twoSum([2, 7, 11, 15], 9), [0, 1]);
assert.deepStrictEqual(twoSum([3, 2, 4], 6), [1, 2]);
