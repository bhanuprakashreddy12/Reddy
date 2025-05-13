document.getElementById("webForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    let formData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value
    };

    let response = await fetch("https://2dir0qjwwd.execute-api.us-east-1.amazonaws.com/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    });

    let result = await response.json();
    document.getElementById("responseMessage").innerText = result.message;
});
