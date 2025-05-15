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
});