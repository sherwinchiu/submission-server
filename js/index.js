const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
const path = require("path");
const fs = require("fs");
const spawn = require("child_process").spawn;

var port = 5500;
var submission_number = 0;
var directory = "../exercise-scripts/week1/question1/answer" + submission_number + ".cpp";
var python_file = "week1-question1.py";

server.listen(port, function () {
    console.log("Server started on port 5500");
});
app.use(express.static(path.join(__dirname, "../")));
app.use(express.static(__dirname));
// Send HTML
app.get("/", function (req, res) {
    res.sendFile(path.join(__dirname, "../index.html"));
});

io.on("connection", (socket) => {
    socket.on("upload", (file, callback) => {
        directory = "../exercise-scripts/week1/question1/answer" + submission_number + ".cpp";
        try {
            fs.writeFile(path.join(__dirname, directory), file.toString(), function (err) {
                if (err) {
                    console.log(err);
                } else {
                    console.log("File " + submission_number.toString() + " written.");
                }
            });
            var process = spawn("python", [path.join(path.join("submission_server", directory), "../" + python_file), submission_number.toString()]);
            process.stdout.on("data", function (data) {
                console.log(data.toString());
            });
            submission_number++;
        } catch (err) {
            console.error(err);
        }
    });
});
