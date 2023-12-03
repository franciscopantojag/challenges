const assert = require('node:assert');

/**
 * @param {string} str
 * @return {string}
 */
const solution = (str) => {
  const re = /[a-z]/i;

  const { initialResult, nonLettersIndexes } = str.split('').reduce(
    (acc, char, index) => {
      const isLetter = re.test(char);
      if (isLetter) {
        acc.initialResult.push(char);
      } else {
        acc.nonLettersIndexes.push({ char, index });
      }
      return acc;
    },
    { initialResult: [], nonLettersIndexes: [] }
  );
  const result = [...initialResult].reverse();
  nonLettersIndexes.forEach(({ index, char }) => {
    result.splice(index, 0, char);
  });
  return result.join('');
};

assert.strictEqual(solution('ab-cd'), 'dc-ba');
assert.strictEqual(solution('a-bC-dEf=ghlj!!'), 'j-lh-gfE=dCba!!');

// ***********************************

class TreeNode {
  constructor(data) {
    this.value = data;
    this.left = null;
    this.right = null;
  }
}

const buildTreeNodeForTest = () => {
  const treeNode = new TreeNode(3);
  const treeNode2 = new TreeNode(9);

  treeNode.left = treeNode2;

  const treeNode3 = new TreeNode(20);

  treeNode.right = treeNode3;

  const treeNode4 = new TreeNode(15);
  const treeNode5 = new TreeNode(7);

  treeNode3.left = treeNode4;
  treeNode3.right = treeNode5;
  return treeNode;
};

/**
 * @param {TreeNode} root
 * @return {number}
 */
const maxDepth = (root) => {
  if (!root) return 0;
  return Math.max(maxDepth(root.right), maxDepth(root.left)) + 1;
};

assert.strictEqual(maxDepth(buildTreeNodeForTest()), 3);
