/**
 * @param {number[]} c
 * @return {number}
 */
const jumpingOnClouds = (c) => {
  if (c.length <= 2) {
    return 1;
  }
  let i = 0;
  let result = 0;
  while (i < c.length - 1) {
    const max = c[i + 2];
    if (max === 0) {
      i += 2;
    } else {
      i++;
    }
    result++;
  }

  return result;
};

console.log(jumpingOnClouds([0, 0, 0, 1, 0, 0])); // 3
console.log(jumpingOnClouds([0, 0, 0, 0, 1, 0])); // 3
console.log(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])); // 4
