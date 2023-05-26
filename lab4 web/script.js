function sendRequest() {
    var expression = document.getElementById("expression").value;

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/api?expression=" + expression, true);

    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var result = JSON.parse(xhr.responseText);
                displayResult(result);
            } else {
                displayError();
            }
        }
    };

    xhr.send();
}

function displayResult(result) {
    var resultDiv = document.getElementById("result");
    resultDiv.innerHTML = result;
}

function displayError() {
    var resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "An error occurred while processing the request.";
}
