const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
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
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};
