#!/usr/bin/node

exports.esrever = function (list) {
  const revlist = [];
  const nbItems = list.length;
  for (let i = nbItems - 1, j = 0; i >= 0; i--, j++) {
    revlist[j] = list[i];
  }
  return revlist;
};
