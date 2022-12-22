#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    if (number === 0) {
      return '0';
    }
    const digits = [];
    while (number > 0) {
      digits.unshift(number % base);
      number = Math.floor(number / base);
    }
    return digits.join('');
  };
};
