var element = document.getElementById("slider");
var page = document.getElementById("page");

slider.onmouseup = function () {
    document.getElementById("form").submit();
}


function ct() {
    var button = document.getElementById("ct-button");
    if ( button.classList.contains("inactive") ) {
        page.value = "ct";
        document.getElementById("form").submit();
    }
}

function ck() {
    var button = document.getElementById("ck-button");
    if ( button.classList.contains("inactive") ) {
        page.value = "ck";
        document.getElementById("form").submit();
    }
}

function dt() {
    var button = document.getElementById("dt-button");
    if ( button.classList.contains("inactive") ) {
        page.value = "dt";
        document.getElementById("form").submit();
    }
}

function dk() {
    var button = document.getElementById("dk-button");
    if ( button.classList.contains("inactive") ) {
        page.value = "dk";
        document.getElementById("form").submit();
    }
}


function weekBack() {
    var button = document.getElementById("wb-button");
    if ( button.classList.contains("active") ) {
        element.value = element.value - 7;
        document.getElementById("form").submit();
    }
}

function dayBack() {
    var button = document.getElementById("db-button");
    if ( button.classList.contains("active") ) {
        element.value = element.value - 1;
        document.getElementById("form").submit();
    }
}

function nextDay() {
    var button = document.getElementById("nd-button");
    if ( button.classList.contains("active") ) {
        element.value++;
        document.getElementById("form").submit();
    }
}

function nextWeek() {
    var button = document.getElementById("nw-button");
    if ( button.classList.contains("active") ) {
        element.value++;
        element.value++;
        element.value++;
        element.value++;
        element.value++;
        element.value++;
        element.value++;
        document.getElementById("form").submit();
    }
}

function about() {
    window.location.href = 'http://127.0.0.1:8000/about/';
}
