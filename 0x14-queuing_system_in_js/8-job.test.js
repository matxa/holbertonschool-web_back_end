import chai from 'chai'

const createPushNotificationsJobs = require('./8-job')
const expect = chai.expect
const queue = require('kue').createQueue()

describe('createPushNotificationsJobs', () => {
	before(() => queue.testMode.enter())
	afterEach(() => queue.testMode.clear())
	after(() => queue.testMode.exit())

	it('displays an error message if jobs is not an array', () => {
		const obj = {
			phoneNumber: '4153518780',
			message: 'This is the code 1234 to verify your account'
		}
		expect(() => createPushNotificationsJobs(obj, queue)).to.throw(Error, 'Jobs is not an array')
	})

	it('creates two new jobs to the queue', () => {
		const jobs = [
			{
				phoneNumber: '4153518780',
				message: 'This is the code 1234 to verify your account'
			},
			{
				phoneNumber: '4153518781',
				message: 'This is the code 4562 to verify your account'
			}
		]
		createPushNotificationsJobs(jobs, queue)
		expect(queue.testMode.jobs.length).to.equal(2)

		expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3')
		expect(queue.testMode.jobs[0].data).to.deep.equal({
			phoneNumber: '4153518780',
			message: 'This is the code 1234 to verify your account'
		})

		expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3')
		expect(queue.testMode.jobs[1].data).to.deep.equal({
			phoneNumber: '4153518781',
			message: 'This is the code 4562 to verify your account'
		})
	})
})
