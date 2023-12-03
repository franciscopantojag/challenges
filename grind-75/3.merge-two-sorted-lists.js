// https://leetcode.com/problems/merge-two-sorted-lists/solutions/?languageTags=javascript

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

const assert = require('node:assert');

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

/**
 * @param {number[]} arr
 */
const buildList = (arr) => {
  const arrNodes = arr.map((n) => new ListNode(n));
  for (let i = 1; i < arr.length; i++) {
    const currentNode = arrNodes[i];
    const previousNode = arrNodes[i - 1];
    previousNode.next = currentNode;
  }
  return arrNodes[0] || new ListNode();
};

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  const list1Numbers = [];
  let currentNode = list1;
  while (currentNode) {
    list1Numbers.push(currentNode.val);
    currentNode = currentNode.next;
  }
  const list2Numbers = [];
  currentNode = list2;
  while (currentNode) {
    list2Numbers.push(currentNode.val);
    currentNode = currentNode.next;
  }

  const finalArr = [...list1Numbers, ...list2Numbers].sort((a, b) => a - b);
  const result = buildList(finalArr);
  console.log(result);
  return result;
};
const l1 = buildList([1, 2, 4]);
const l2 = buildList([1, 3, 4]);
mergeTwoLists(l1, l2);

//////////////////////////////
const mergeTwoLists2 = (list1, list2) => {
  // initialize new linked list
  let head = new ListNode(null);

  // new pointer
  let current = head;

  // loop while both lists are not null (did not reach end)
  while (list1 && list2) {
    // check which val is lower and point current to it
    // move the pointer on the lower list
    if (list1.val <= list2.val) {
      current.next = list1;
      list1 = list1.next;
    } else {
      current.next = list2;
      list2 = list2.next;
    }

    // move the current pointer
    current = current.next;
  }

  // determine which node is not null
  let remaining = list1 || list2;

  // set current to the remaining list
  current.next = remaining;

  // return next because head was initialized to null
  return head.next;
};

const list1 = [1, 2, 4];
const list2 = [1, 3, 4];
assert.deepStrictEqual(
  mergeTwoLists2(buildList(list1), buildList(list2)),
  buildList([1, 1, 2, 3, 4, 4])
);
