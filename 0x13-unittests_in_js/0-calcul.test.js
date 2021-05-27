const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('(1, 3) should return -> 4', () => {
    assert.equal(calculateNumber(1, 3), 4);
  });
  it('(1, 3.7) should return -> 5', () => {
    assert.equal(calculateNumber(1, 3.7), 5);
  });
  it('(1.2, 3.7) should return -> 5', () => {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });
  it('(1.5, 3.7) should return -> 6', () => {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
});
