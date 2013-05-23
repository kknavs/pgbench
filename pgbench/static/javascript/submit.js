$(document).ready(function () {
        var upload = $("#uploadForm");
        var input = $("#inputForm");
        upload.hide();
        input.hide();

        var uploadBtn = $("#upload");
        var inputBtn = $("#input");
        uploadBtn.click(function () {
            input.hide();
            upload.show();
        });
        inputBtn.click(function () {
            input.show();
            upload.hide();
        });
    }
)
;
