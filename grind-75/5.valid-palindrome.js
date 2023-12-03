// https://leetcode.com/problems/valid-palindrome/description/

const assert = require("node:assert");

/**
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = (s) => {
  const re = /[0-9]|[a-z]/;
  const arr = s
    .toLowerCase()
    .split("")
    .filter((char) => re.test(char));
  const arr2 = [...arr].reverse();

  return arr.join("") === arr2.join("");
};

assert.strictEqual(isPalindrome("A man, a plan, a canal: Panama"), true);
assert.strictEqual(isPalindrome("race a car"), false);
