// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/?languageTags=javascript
const assert = require('node:assert');

/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = (prices) => {
  let maxProfit = 0;
  let minPrice = prices[0];
  for (let i = 1; i < prices.length; i++) {
    const currentPrice = prices[i];
    const currentProfit = currentPrice - minPrice;
    if (currentProfit > maxProfit) {
      maxProfit = currentProfit;
    }
    if (currentPrice < minPrice) {
      minPrice = currentPrice;
    }
  }
  return maxProfit;
};

assert.strictEqual(maxProfit([7, 1, 5, 3, 6, 4]), 5);
assert.strictEqual(maxProfit([7, 6, 4, 3, 1]), 0);
