#!/usr/bin/node
exports.esrever = function (list) {
  const second = [];
  for (let i = list.legth; i >= 0; i++) {
    second.push(list[i]);
  }
  return (second);
};
