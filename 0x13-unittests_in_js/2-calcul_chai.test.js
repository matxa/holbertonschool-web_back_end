const chai = require('chai');
const calculateNumber = require('./2-calcul_chai');

const { expect } = chai;

describe('calculateNumber', () => {
  it('...', () => {
    expect(calculateNumber('SUM', 1, 3)).to.be.equal(4);
  });
  it('...', () => {
    expect(calculateNumber('SUM', 1, 3.7)).to.be.equal(5);
  });
  it('...', () => {
    expect(calculateNumber('SUM', 1.2, 3.7)).to.be.equal(5);
  });
  it('...', () => {
    expect(calculateNumber('SUM', 1.5, 3.7)).to.be.equal(6);
  });
  it('...', () => {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.be.equal(6);
  });
  it('...', () => {
    expect(calculateNumber('SUM', 1.4, 0)).to.be.equal(1);
  });
  it('...', () => {
    expect(calculateNumber('SUM', 0, 1.4)).to.be.equal(1);
  });
});

describe('calculateNumber', () => {
  it('...', () => {
    expect(calculateNumber('SUBTRACT', 1, 3)).to.be.equal(-2);
  });
  it('...', () => {
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.be.equal(-3);
  });
  it('...', () => {
    expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.be.equal(-3);
  });
  it('...', () => {
    expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.be.equal(-2);
  });
  it('...', () => {
    expect(calculateNumber('SUBTRACT', 4.5, 1.5)).to.be.equal(3);
  });
  it('...', () => {
    expect(calculateNumber('SUBTRACT', 1.4, 0)).to.be.equal(1);
  });
  it('...', () => {
    expect(calculateNumber('SUBTRACT', 0, 1.4)).to.be.equal(-1);
  });
});

describe('calculateNumber', () => {
  it('...', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.be.equal(0.2);
  });
  it('...', () => {
    expect(calculateNumber('DIVIDE', 3, 1)).to.be.equal(3);
  });
  it('...', () => {
    expect(calculateNumber('DIVIDE', 1.5, 3.7)).to.be.equal(0.5);
  });
  it('...', () => {
    expect(calculateNumber('DIVIDE', 1.4, 0.4)).to.be.equal('Error');
  });
  it('...', () => {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.be.equal('Error');
  });
  it('...', () => {
    expect(calculateNumber('DIVIDE', 0, 1.4)).to.be.equal(0);
  });
});
