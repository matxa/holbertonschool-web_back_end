const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', () => {
  it('...', () => {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUM', 1, 3.7), 5);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUM', 1.4, 0), 1);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUM', 0, 1.4), 1);
  });
});

describe('calculateNumber', () => {
  it('...', () => {
    assert.equal(calculateNumber('SUBTRACT', 1, 3), -2);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUBTRACT', 1, 3.7), -3);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUBTRACT', 4.5, 1.5), 3);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUBTRACT', 1.4, 0), 1);
  });
  it('...', () => {
    assert.equal(calculateNumber('SUBTRACT', 0, 1.4), -1);
  });
});

describe('calculateNumber', () => {
  it('...', () => {
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });
  it('...', () => {
    assert.equal(calculateNumber('DIVIDE', 3, 1), 3);
  });
  it('...', () => {
    assert.equal(calculateNumber('DIVIDE', 1.5, 3.7), 0.5);
  });
  it('...', () => {
    assert.equal(calculateNumber('DIVIDE', 1.4, 0.4), 'Error');
  });
  it('...', () => {
    assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
  it('...', () => {
    assert.equal(calculateNumber('DIVIDE', 0, 1.4), 0);
  });
});
