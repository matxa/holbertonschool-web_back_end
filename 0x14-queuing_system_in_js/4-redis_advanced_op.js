import redis from "redis";
const client = redis.createClient();

client.on("ready", function() {
  console.log(`Redis client connected to the server`);
})

client.on("error", function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

// hash Set

client.hset("city", "Portland", '50', redis.print);
client.hset("city", "Seattle", '80', redis.print);
client.hset("city", "New York", '20', redis.print);
client.hset("city", "Bogota", '20', redis.print);
client.hset("city", "Cali", '40', redis.print);
client.hset("city", "Paris", '2', redis.print);

// hash get all
client.hgetall("city", (err, res) => {
  if (err) {
    console.log("can't get 'city' HSET",);
  } else {
    console.log(res);
  }
});
