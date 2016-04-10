var express = require("express");
var helper = require("./helper");

var get_results = helper.get_results;
var index = helper.index;

var app = express();

app.get("/", function(req, res) {
  res.json({
    "message": "Welcome to the app"
  });
});

app.get("/index", function(req, res) {
  index(function(result) {
    res.json({
      "message": result
    });
  });
});

app.get("/results/:id", function(req, res) {
  var id = req.params.id;
  console.log("Req: ", req.params);
  console.log("Id: ", id);
  get_results(id, function(result) {
    res.json({
      "message": result
    });
  });
});

app.listen(3000, function() {
  console.log("[APP] running.");
});
