const socket = io();
const myCodeMirror = CodeMirror($("#code")[0], {
    value: "#include <iostream>\n\nint main(){\n\t\n\treturn 0;\n}",
    indentUnit: 4,
    lineNumbers: true,
    mode: "text/x-c++src",
});

// socket.emit("give-page"){
//
// }

var path = window.location.pathname;
var page = path.split("/");
page[3] = page[3].split(".")[0];

var clicking = false;

var left_div = $("#left-div");
var right_div = $("#right-div");
var code_block = $("#code");
var horizontal_slide = $("#h-slide");
var vertical_slide = $("#v-slide");
var console_block = $("#console");

$(vertical_slide).mousedown(function (e) {
    var dragX = e.clientX;
    clicking = true;
    $(document).mousemove(function (e) {
        if (clicking) {
            left_div.css("width", left_div.outerWidth() + e.clientX - dragX + "px");
            left_div.outerWidth(dragX);
            // right_div.css("width", left_div.outerWidth() + e.clientX - dragX + "px");
            // right_div.outerWidth(dragX);
            dragX = e.clientX;
        }
    });
});
$(horizontal_slide).mousedown(function (e) {
    var dragY = e.clientY;
    clicking = true;
    $(document).mousemove(function (e) {
        if (clicking) {
            code_block.css("height", code_block.outerHeight() + e.clientY - dragY + "px");
            code_block.outerHeight(dragY);
            dragY = e.clientY;
        }
    });
});
$(document).mouseup(function (e) {
    clicking = false;
});
$(document).mouseleave(function (e) {
    clicking = false;
});

socket.emit("give-page", page[2], page[3], (status) => {
    console.log(status);
});

socket.on("page-content", function (markdown) {
    $("#left-div").append(markdown);
});
