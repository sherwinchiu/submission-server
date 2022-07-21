const socket = io();

function upload(files) {
    socket.emit("upload", files[0], (status) => {
        console.log(status);
    });
}
