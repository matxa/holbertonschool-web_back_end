const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const sum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${sum}`);
}

sendPaymentRequestToApi(100, 20);

module.exports = sendPaymentRequestToApi;
