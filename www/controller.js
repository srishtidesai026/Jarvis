$(document).ready(function () {

    // Expose the function globally
    eel.expose(displayMsg);

    function displayMsg(msg) {
        console.log("displayMsg called with:", msg);  // Debug check
        $(".sirimsg p").html(msg.replace(/\n/g, "<br>").replace(/\*/g, "•"));
        $(".sirimsg").textillate('start');
    }

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
});




