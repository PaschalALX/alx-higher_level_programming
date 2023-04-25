#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];

try {
  const data = fs.readFileSync(path, 'utf-8');
  console.log(data);
} catch (err) {
  const errFmt = `{ Error: ${err.message} at Error (native)\nerrno: ${err.errno},\n code: '${err.code}',\n syscall: '${err.syscall}',\n path: '${err.path}' }`;
  console.log(errFmt);
}
