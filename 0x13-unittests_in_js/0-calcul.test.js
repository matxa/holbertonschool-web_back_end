const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('...', () => {
    assert.equal(calculateNumber(1, 3), 4);
  });
  it('...', () => {
    assert.equal(calculateNumber(1, 3.7), 5);
  });
  it('...', () => {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });
  it('...', () => {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
  it('...', () => {
    assert.equal(calculateNumber(1.4, 4.5), 6);
  });
  it('...', () => {
    assert.equal(calculateNumber(1.4, 0), 1);
  });
  it('...', () => {
    assert.equal(calculateNumber(0, 1.4), 1);
  });
});
