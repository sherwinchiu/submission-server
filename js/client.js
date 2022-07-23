const socket = io();

function upload(files, week_num, question_num) {
    socket.emit("upload", files[0], week_num, question_num, (status) => {
        console.log(status);
    });
}
function change_text(question_num) {}

// socket.on(""){

// }
