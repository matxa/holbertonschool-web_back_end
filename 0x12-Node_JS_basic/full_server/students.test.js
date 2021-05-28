const chai = require('chai');
const chaiHttp = require('chai-http');

process.argv[2] = './database.csv';

import app from './server';

chai.use(chaiHttp);
chai.should();

describe('Full HTTP server using Express', () => {

  describe('/students/:major endpoint', () => {
    describe('When the database is available', () => {
      before(() => {
        process.argv[2] = './database.csv';
      });
      it('Returns the right error when the parameter is wrong', (done) => {
        chai.request(app)
          .get('/students/BLABLA')
          .end((error, response) => {
            chai.expect(response.statusCode).to.equal(500);
            chai.expect(response.text).to.equal(`Major parameter must be CS or SWE`);
            done();

          });
      });
    });
  });
});
