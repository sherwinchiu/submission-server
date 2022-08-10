const socket = io();
// var question = document.getElementById("current-question");

function upload(files, week_num, question_num) {
    socket.emit("upload", files[0], week_num, question_num, (status) => {
        console.log(status);
    });
}
function change_text(week_num, question_num) {
    directory = "./templates/week" + week_num + "/question" + question_num + ".html";
    location.href = directory;
}
