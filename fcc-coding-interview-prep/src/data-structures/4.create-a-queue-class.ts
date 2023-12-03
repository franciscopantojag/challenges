export class Queue {
  private collection: any[] = [];

  enqueue(element: any) {
    return this.collection.push(element);
  }

  dequeue() {
    return this.collection.shift();
  }

  front() {
    return this.collection[0];
  }

  size() {
    return this.collection.length;
  }

  isEmpty() {
    return this.collection.length === 0;
  }
}

export const test = () => {
  console.log('sjdbs');
};
