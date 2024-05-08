const serverHost = 'http://127.0.0.1:5000';
// logging.getLogger('flask_cors').level = logging.DEBUG

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === 'getData') {
        const url_fetch = request.url;

        // Send a POST request to your Flask server
        fetch(serverHost + "/home", {
            method: "POST",
            headers: {
                "Content-Type": 'application/json'
            },
            body: JSON.stringify({ url: url_fetch }), // Send the URL as JSON in the request body

        })
        // Send a GET request to your Flask server
        fetch(serverHost + '/home')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                sendResponse(data); // Send the fetched data as a response
                console.log(`Data ${data}`);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                sendResponse({ error: error.message }); // Send an error message as a response
            });


        // Return true to indicate that sendResponse will be called asynchronously
        return true;
    }
});
