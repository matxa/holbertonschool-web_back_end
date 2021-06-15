import kue from 'kue';

const queue = kue.createQueue();

const info = {
  phoneNumber: "1234567890",
  message: "string",
}

const push_notification_code = queue.create('push_notification_code', info).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${push_notification_code.id}`);
  } else {
    console.log("Notification job failed");
  }
}).on("complete", () => {
  console.log("Notification job completed");
});
