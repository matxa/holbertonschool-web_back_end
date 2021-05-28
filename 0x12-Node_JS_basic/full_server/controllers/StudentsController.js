import readDatabase from '../utils';

const DB = process.argv[2];
let _DB = null;
if (DB) {
  _DB = DB.replace('./', '');
}

const __DB = _DB == null ? 'database.csv' : _DB;

export default class StudentsController {
  static getAllStudents(equest, response) {
    readDatabase(__DB)
      .then((fields) => {
        const output = `Number of students: ${fields[0].list.length + fields[1].list.length}\nNumber of students in ${fields[0].name}: ${fields[0].list.length}. List: ${fields[0].list}\nNumber of students in ${fields[1].name}: ${fields[1].list.length}. List: ${fields[1].list}`;
        response.status(200).send(`This is the list of our students\n${output}`);
      }).catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    if (request.params.major) {
      if (request.params.major === 'CS' || request.params.major === 'SWE') {
        readDatabase(__DB)
          .then((fields) => {
            if (request.params.major === 'CS') {
              response.status(200).send(`List: ${fields[0].list}`);
            } else if (request.params.major === 'SWE') {
              response.status(200).send(`List: ${fields[1].list}`);
            }
          }).catch(() => {
            response.status(500).send('Cannot load the database');
          });
      } else {
        response.status(500).send('Major parameter must be CS or SWE\n');
      }
    }
  }
}
