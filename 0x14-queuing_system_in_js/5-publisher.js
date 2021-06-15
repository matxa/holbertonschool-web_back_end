import redis from "redis";
import util from 'util';

const client = redis.createClient();
const setTimeoutPromise = util.promisify(setTimeout);


client.on("ready", function() {
  console.log(`Redis client connected to the server`);
})

client.on("error", function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

function publishMessage(message, time) {
  setTimeoutPromise(time).then(() => {
    console.log(`About to send ${message}`);
    client.publish("holberton school channel", message);
  });
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
