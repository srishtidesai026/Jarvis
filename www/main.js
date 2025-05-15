$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'bounceIn',
        },
        out: {
            effect: 'bounceOut',
        },
    })


    /*siri config*/
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });

    /*siri msg animation*/
    $('.sirimsg').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeInUp',
            sync: true
        },
        out: {
            effect: 'fadeOutUp',
            sync: true
        },
    })


    /* mic button */
    $("#mic").click(function () {
        $("#oval").attr("hidden", true);
        $("#siriwave").attr("hidden", false);
        eel.playAssistantSound()
        eel.allCommands()
    });


    /*shortcut key for mai*/
    function doc_keyUp(e) {
        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound()
            $("#oval").attr("hidden", true);
            $("#siriwave").attr("hidden", false);
            eel.allCommands()()  //listens to our query
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);


    // to be displayed after the search operation via text is over
    function PlayAssistant(message) {

        if (message.trim() !== "") {
            $("#oval").attr("hidden", true);
            $("#siriwave").attr("hidden", false);

            $("#greeting").hide();  // Hide greeting ONLY, not other messages

            eel.allCommands(message); // Process user command

            $("#chatbox").val("");  // Clear input after sending
            showHideSendButton();  // Ensure correct button visibility
        }
    }


    function showHideSendButton() {
        let message = $("#chatbox").val().trim();
        if (message === "") {
            $("#mic").show();
            $("#send").hide();  // Use .hide() instead of attr("hidden", true)
        } else {
            $("#mic").hide();
            $("#send").show();  // Use .show() instead of attr("hidden", false)
        }
    }

    // Detect typing in chatbox
    $("#chatbox").on("input", function () {
        showHideSendButton();
        $("#greeting").hide();
    });


    // Handle send button click
    $("#send").click(function () {
        let message = $("#chatbox").val();
        PlayAssistant(message);
    });


    // search activated for 'enter' key
    $("#chatbox").keypress(function (e) {

        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val();
            PlayAssistant(message);
        }
    });

});