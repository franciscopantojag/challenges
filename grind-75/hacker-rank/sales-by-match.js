/**
 * @param {number[]} sockColors
 * @return {number}
 */

const findPairs = (sockColors) => {
  const { result } = sockColors.reduce(
    ({ set, result }, nColor) => {
      if (set.has(nColor)) {
        result += 1;
        set.delete(nColor);
      } else {
        set.add(nColor);
      }
      return { set, result };
    },
    { set: new Set(), result: 0 }
  );

  return result;
};
console.log(findPairs([1, 2, 1, 2, 1, 3, 2])); // 2
