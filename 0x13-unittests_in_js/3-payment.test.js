const sinon = require('sinon');
const chai = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

const { expect } = chai;

describe('calculateNumber', () => {
  it('...', () => {
    const calcSpy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    expect(calcSpy.calledWith('SUM', 100, 20)).to.be.true;
  });
});
