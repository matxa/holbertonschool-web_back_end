const fs = require('fs');
const util = require('util');

const readFile = util.promisify(fs.readFile);

module.exports = async function countStudents(path) {
  return readFile(path, 'utf-8').then((data) => {
    const records = data.split('\n');
    const SWE = {
      name: 'SWE',
      list: [],
    };
    const CS = {
      name: 'CS',
      list: [],
    };
    const fields = [CS, SWE];
    for (const i in records) {
      if (i > 0) {
        const [student, , , field] = records[i].split(',');
        if (field === 'CS') {
          CS.list.push(` ${student}`);
        } else if (field === 'SWE') {
          SWE.list.push(` ${student}`);
        }
      }
    }
    fields[0].list[0] = fields[0].list[0].trim();
    fields[1].list[0] = fields[1].list[0].trim();
    console.log(`Number of students: ${fields[0].list.length + fields[1].list.length}`);
    console.log(`Number of students in ${fields[0].name}: ${fields[0].list.length}. List: ${fields[0].list}`);
    console.log(`Number of students in ${fields[1].name}: ${fields[1].list.length}. List: ${fields[1].list}`);
    const output = `Number of students: ${fields[0].list.length + fields[1].list.length}\nNumber of students in ${fields[0].name}: ${fields[0].list.length}. List: ${fields[0].list}\nNumber of students in ${fields[1].name}: ${fields[1].list.length}. List: ${fields[1].list}`;
    return output;
  }).catch(() => { throw new Error('Cannot load the database'); });
};
