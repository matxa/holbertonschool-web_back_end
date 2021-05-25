import fs from 'fs';
import util from 'util';

const readFile = util.promisify(fs.readFile);

export default function readDatabase(path) {
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
    return fields;
  }).catch((err) => { throw new Error(err); });
}
