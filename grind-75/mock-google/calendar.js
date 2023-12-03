class Person {
  /**
   * @param {string[][]} meetings
   * @param {string[]} preference
   */
  constructor(meetings, preference) {
    this.meetings = meetings;
    this.preference = preference;
  }
}
const person1 = new Person(
  [
    ['9:00', '10:30'],
    ['12:00', '13:00'],
    ['16:00', '18:00'],
  ],
  ['9:00', '20:00']
);

const person2 = new Person(
  [
    ['10:00', '11:30'],
    ['12:30', '14:30'],
    ['14:30', '15:00'],
    ['16:00', '17:00'],
  ],
  ['10:00', '18:30']
);

/**
 * @param {string} timeStr
 */
const getFloatTime = (timeStr) => {
  const [hoursStr, minutesStr] = timeStr.split(':');
  const hours = parseInt(hoursStr);
  const minutes = parseInt(minutesStr) / 60;
  return hours + minutes;
};

/**
 * @param {Person} person
 */
const getFreeTime = (person) => {
  const timeBetweenMeetings = person.meetings.reduce(
    (acc, timeBlock, index, arr) => {
      const rawEndTime = arr[index + 1]?.[0];
      if (!rawEndTime) return acc;
      const startTime = getFloatTime(timeBlock[1]);
      const endTime = getFloatTime(rawEndTime);
      if (startTime === endTime) return acc;
      const freeBlock = [startTime, endTime];
      acc.push(freeBlock);
      return acc;
    },
    []
  );

  const startDay = getFloatTime(person.preference[0]);
  const firstMeetingStartTime = getFloatTime(person.meetings[0][0]);
  const hasStartBlock = firstMeetingStartTime > startDay;
  if (hasStartBlock) {
    timeBetweenMeetings.unshift([startDay, firstMeetingStartTime]);
  }

  const endDay = getFloatTime(person.preference[1]);
  const lastMeetingEndTime = getFloatTime(
    person.meetings[person.meetings.length - 1][1]
  );
  const hasEndBlock = endDay > lastMeetingEndTime;
  if (hasEndBlock) {
    timeBetweenMeetings.push([lastMeetingEndTime, endDay]);
  }
  return timeBetweenMeetings;
};

/**
 * @param {Person} p1
 * @param {Person} p2
 * @param {number} mins
 */
const findTime = (p1, p2, mins) => {
  const p1FreeTime = getFreeTime(p1);
  const p2FreeTime = getFreeTime(p2);
  return [p1FreeTime, p2FreeTime];
};
console.log(findTime(person1, person2, 30));
