import assert from 'assert';

export default class HolbertonCourse {
  constructor(name, length, students) {
    assert(typeof (name), 'string');
    assert(typeof (length), 'number');
    assert(typeof (students), 'list');
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() { return this._name; }

  set name(name) { this._name = name; }

  get length() { return this.length; }

  set length(length) { this._length = length; }

  get students() { return this._students; }

  set students(students) { this._students = students; }
}
