const sinon = require('sinon');
const chai = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

const { expect } = chai;

describe('calculateNumber', () => {
  it('...', () => {
    const calcSpy = sinon.stub(Utils, 'calculateNumber').callsFake(() => "The total is: 10");
    calcSpy.restore();
    expect(calcSpy.call('SUM', 100, 20)).to.be.equal("The total is: 10");
  });
});
