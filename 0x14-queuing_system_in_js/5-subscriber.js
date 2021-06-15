import redis from "redis";
const client = redis.createClient();

client.on("ready", function() {
  console.log(`Redis client connected to the server`);
})

client.on("error", function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on("message", (channel, message) => {
  console.log(message);

  if (message == 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});

client.subscribe("holberton school channel");
