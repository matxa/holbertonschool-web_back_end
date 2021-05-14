export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Length must be a number');
    if (!Array.isArray(students)) throw TypeError('Students must be an array');
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
