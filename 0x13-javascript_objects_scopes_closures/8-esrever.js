#!/usr/bin/node
exports.esrever = function (list) {
  const second = [];
  for (let i = list.length - 1; i >= 0; i--) {
    second.push(list[i]);
  }
  return (second);
};
