/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
const solution = (str1, str2) => {
  const buildStr = (str) => {
    const strArr = str.split('');
    const i = strArr.findIndex((ch, index, c) => {
      const prev = c[index - 1];
      return ch === '#' && prev?.match(/[a-z]/i);
    });
    if (i === -1) return str;
    strArr.splice(i - 1, 2);
    const newStr = strArr.join('');
    return buildStr(newStr);
  };
  return buildStr(str2) === buildStr(str1);
  // return buildStr(str1);
};

console.log(solution('a#c', 'b'));
