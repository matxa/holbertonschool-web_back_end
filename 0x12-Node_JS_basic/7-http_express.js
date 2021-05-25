const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (_, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (_, res) => {
  countStudents('database.csv').then((data) => res.send(data));
});

app.listen(1245);

module.exports = app;
