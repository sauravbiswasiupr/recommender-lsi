var zerorpc = require("zerorpc");

var client  = new zerorpc.Client();
client.connect("tcp://127.0.0.1:4242")

function get_results(id, cb) {
  client.invoke("recommend", id, function(err, res, more) {
    console.log("Error: ", err);
    console.log("Result: ", res);
    if (err)
      cb(null);
    else {
      var result = res;
      cb(result);
    }
  });
};
exports.get_results = get_results;

function index(cb) {
  client.invoke("index", function(err, res, more) {
    if (err)
      cb(err)
    else {
      cb(res);
    }
  });
};
exports.index = index;
