let timeoutID;
let timeout = 15000;


function setup() {
    console.log("window setup");
    timeoutID = window.setTimeout(poller, timeout);
    displayMessages();
}


function addMessage() {
    const message = document.getElementById("message").value;
    const author = window. location. href.split("/").pop();
    console.log(`${message} ${author}`);
    
    fetch("/new_message/", { 
        method: "post", 
        headers: { "Content-type": "application/json; charset=UTF-8" }, 
        body: JSON.stringify({
            username: author,
            message: message
        })
    }) 
    .then(() => {
        console.log("new messge fetched");
        clearInput();
        displayMessages();
    })
    .catch(() => { 
        document.getElementById("chat_window").value = "message was not added properly"; 
    }); 
}

function clearInput() {
    console.log("new messge cleared");
    document.getElementById("message").value = "";
}

function displayMessages() {
    fetch("/messages/") 
        .then((response) => { 
            return response.json(); 
        }) 
        .then((results) => { 
            let chat_window = document.getElementById("chat_window"); 
 
            let messages = ""; 
            for (let index in results) { 
                current_set = results[index]; 
                for (let key in current_set) { 
                    author = key; 
                    author = author.toUpperCase();
                    message = current_set[key]; 
                    messages += `${author}:\n${message}\n\n`; 
                } 
            } 
            chat_window.value = messages; 
        }) 
        .catch(() => { 
            chat_window.value = "error retrieving messages from server"; 
        }); 
}


function poller() {
    displayMessages();
    timeoutID = window.setTimeout(poller, timeout);
}


window.addEventListener('load', setup);