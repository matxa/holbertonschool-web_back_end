const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (req.url === '/students') {
    countStudents('database.csv')
      .then((data) => {
        res.write(`This is the list of our students\n${data}`);
        res.end();
      })
      .catch((err) => console.log(err));
  }
});
app.listen(1245);

module.exports = app;
