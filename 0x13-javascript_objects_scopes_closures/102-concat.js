#!/usr/bin/node
const fs = require('fs/promises');
const path = require('path');
const { argv } = process;
const argc = argv.length;

async function exec (fileA, fileB, fileC) {
  const fileAContent = await fs.readFile(path.resolve(fileA), 'utf-8');
  const fileBContent = await fs.readFile(path.resolve(fileB), 'utf-8');
  const content = `${fileAContent}\n${fileBContent}`;
  await fs.writeFile(path.resolve(fileC), content);
}

if (argc === 5) {
  exec(argv[2], argv[3], argv[4]);
}
