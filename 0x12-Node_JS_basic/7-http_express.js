const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const FILE = process.argv[2];

app.get('/', (_, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (_, res) => {
  countStudents(FILE)
    .then((data) => res.send(`This is the list of our students\n${data}`))
    .catch(() => {
      res.write('This is the list of our students\n');
      res.write('Cannot load the database');
      res.end();
    });
});

app.listen(1245);

module.exports = app;
