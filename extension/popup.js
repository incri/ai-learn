document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("popup-button").addEventListener("click", toggleDivVisibility);
});

function toggleDivVisibility() {
    chrome.tabs.executeScript({
        code: `
            function toggleDivVisibilityById(id1, id2) {
                const div1 = document.getElementById(id1);
                const div2 = document.getElementById(id2);
                if (div1) {

                    if (div1.style.display === "") {
                        div1.style.display = "block";
                    }

                    if (div1.style.display === "block") {
                        div1.style.display = "none";
                    } else {
                        if (div1.style.display === "none") {
                            div1.style.display = "block";
                        };
                    }
                }
            }
            toggleDivVisibilityById("header-container", "kernel_indicator");
        `
    });
}
