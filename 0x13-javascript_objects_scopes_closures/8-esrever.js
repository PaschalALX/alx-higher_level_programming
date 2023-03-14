exports.esrever = function (list) {
  const len = list.length;
  for (let i = 0, j = len - 1; i < (len / 2); i++, j--) {
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }
  return list;
};
