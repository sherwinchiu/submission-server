const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
const path = require("path");
const fs = require("fs");
const spawn = require("child_process").spawn;
const md = require("markdown-it")()
    .use(require('markdown-it-highlightjs'), {});

var port = 5500;
var submission_number = 1;
var directory = "../exercise-scripts/week1/question1/answer" + submission_number + ".cpp";
var python_file = "week1-question1.py";
var question = "./exercise-scripts/week1/question1/tests.md";

server.listen(port, function () {
    console.log("Server started on port 5500");
});
app.use(express.static(path.join(__dirname, "../")));
app.use(express.static(__dirname));
// Send HTML
app.get("/", function (req, res) {
    try {
        let index = fs.readFileSync("./templates/index.html", "utf-8");
        let markdown = fs.readFileSync(question, "utf-8");
        res.send(index.replace("{{ MD_CONTENT }}", md.render(markdown)));
    } catch (err) {
        console.error(err);
    }
});

io.on("connection", (socket) => {
    socket.on("upload", (file, week_num, question_num, callback) => {
        try {
            python_file = "week" + week_num + "-question" + question_num + ".py";
            directory = "../exercise-scripts/week" + week_num + "/question" + question_num + "/answer" + submission_number + ".cpp";
            fs.writeFile(path.join(__dirname, directory), file.toString(), function (err) {
                if (err) {
                    console.log(err);
                } else {
                    console.log("File " + submission_number.toString() + " written.");
                }
                submission_number++;
            });
            var process = spawn("python", [path.join(path.join("submission_server", directory), "../" + python_file), submission_number.toString()]);
            process.stdout.on("data", function (data) {
                console.log(data.toString());
            });
        } catch (err) {
            console.error(err);
        }
    });
});
