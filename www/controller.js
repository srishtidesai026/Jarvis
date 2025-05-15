$(document).ready(function () {

    // Expose the function globally first
    eel.expose(displayMsg);

    function displayMsg(msg) {

        console.log("displayMsg called with:", msg);  // Debug check
        $(".sirimsg p").text(msg);
        $(".sirimsg").textillate('start');
    }

    eel.expose(showHood);
    function showHood() {
        $("#oval").attr("hidden", false);
        $("#siriwave").attr("hidden", true);
    }
});



