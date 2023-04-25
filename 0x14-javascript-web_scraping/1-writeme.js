#!/usr/bin/node

const fs = require('fs');

const path = process.argv[2];
const data = process.argv[3];

try {
  fs.writeFileSync(path, data, 'utf-8');
} catch (err) {
  const errFmt = `{ Error: ${err.message} at Error (native)\nerrno: ${err.errno},\n code: '${err.code}',\n syscall: '${err.syscall}',\n path: '${err.path}' }`;
  console.log(errFmt);
}
