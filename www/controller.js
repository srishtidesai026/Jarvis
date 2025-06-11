$(document).ready(function () {

    // Expose the function globally
    eel.expose(displayMsg);



    function displayMsg(msg) {
        console.log("displayMsg called with:", msg);
        const element = $(".siri-message");
        // Stop any running animation
        element.textillate('stop');
        // Set new content
        element.html(msg.replace(/\n/g, "<br>").replace(/\*/g, "•"));
        // Reinitialize textillate
        element.textillate({
            in: {
                effect: 'fadeInUp',
                delayScale: 1.5,
                delay: 50,
                sync: false
            },
            out: {
                effect: 'fadeOut',
                sync: false
            },
            loop: false,
            autoStart: true
        });
        // Start animation
        element.textillate('start');
    }
    // console.log("displayMsg called with:", msg);  // Debug check
    // $(".sirimsg p").html(msg.replace(/\n/g, "<br>").replace(/\*/g, "•"));
    // $(".sirimsg").textillate('start');


    eel.expose(showHood);
    function showHood() {
        $("#oval").attr("hidden", false);
        $("#siriwave").attr("hidden", true);
    }

    eel.expose(senderText);
    function senderText(message) {
        var chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `<div class="row justify-content-end mb-4">
                <div class="width-size">
                    <div class="sender_message">${message}</div>
                </div>
            </div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    eel.expose(receiverText);
    function receiverText(message) {
        const chatBox = document.getElementById("chat-canvas-body");

        if (message.trim() !== "") {
            const safeMsg = message
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/\n/g, "<br>");

            chatBox.innerHTML += `
            <div class="row justify-content-start mb-4">
                <div class="width-size">
                    <div class="receiver_message" style="white-space: pre-line;">${safeMsg}</div>
                </div>
            </div>
        `;

            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }


    // Hide Loader and display Face Auth animation
    eel.expose(hideLoader)
    function hideLoader() {

        $("#Loader").attr("hidden", true);
        $("#FaceAuth").attr("hidden", false);

    }

    // Hide Face auth and display Face Auth success animation
    eel.expose(hideFaceAuth)
    function hideFaceAuth() {

        $("#FaceAuth").attr("hidden", true);
        $("#FaceAuthSuccess").attr("hidden", false);

    }

    // Hide success and display 
    eel.expose(hideFaceAuthSuccess)
    function hideFaceAuthSuccess() {

        $("#FaceAuthSuccess").attr("hidden", true);
        $("#HelloGreet").attr("hidden", false);

    }


    // Hide Start Page and display blob
    eel.expose(hideStart)
    function hideStart() {

        $("#Start").attr("hidden", true);

        setTimeout(function () {
            $("#oval").addClass("animate__animated animate__zoomIn");

        }

            , 1000)
        setTimeout(function () {
            $("#oval").attr("hidden", false);
        }

            , 1000)
    }
});




