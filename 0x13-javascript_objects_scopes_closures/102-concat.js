#!/usr/bin/node
const fs = require('fs');
const path = require('path');
const { argv } = process;
const argc = argv.length;

function exec (fileA, fileB, fileC) {
  let output = '';
  fs.readFile(path.resolve(fileA), 'utf-8', function (err, data) {
    if (err) throw err;
    output = output.concat(data, '\n');
    fs.readFile(path.resolve(fileB), 'utf-8', function (err2, data2) {
      if (err2) throw err2;
      output = output.concat(data2, '\n');

      fs.writeFile(path.resolve(fileC), output, function (err3) {
        if (err3) throw err3;
      });
    });
  });
}

if (argc === 5) {
  exec(argv[2], argv[3], argv[4]);
}
