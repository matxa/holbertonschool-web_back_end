import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(request, response) {
    readDatabase("../../database.csv")
      .then((fields) => {
        response.send("This is the list of our students");
        const output = `Number of students: ${fields[0].list.length + fields[1].list.length}\nNumber of students in ${fields[0].name}: ${fields[0].list.length}. List: ${fields[0].list}\nNumber of students in ${fields[1].name}: ${fields[1].list.length}. List: ${fields[1].list}`;
        response.status(200).send(output);
    }).catch(() => {
      response.status(500).send("Cannot load the database");
    });
  }

  static getAllStudentsByMajor(request, response) {
    if (request.query.major) {
      if (request.query.major === 'CS' || request.query.major === 'SWE') {
        readDatabase("../../database.csv")
          .then((fields) => {
            if (request.query.major === 'CS') {
              response.status(200).send(`List: ${fields[0].list}`);
            } else if (request.query.major === 'SWE') {
              response.status(200).send(`List: ${fields[1].list}`);
            }
          }).catch(() => {
            response.status(500).send("Cannot load the database");
          })
      } else {
        response.status(500).send("Major parameter must be CS or SWE");
      }
    }
  }
}
