const button = document.getElementById('button');
const summaryDiv = document.getElementById('summary');
const url_input = document.getElementById('url')
button.addEventListener('click', changeText)

function changeText(){
    // Start runnint the python script
    
    const url = url_input.value; // Get the value of the input field 'url'
    chrome.runtime.sendMessage({ action: 'getData', url: url }, function(response) {
        const data = response.message;
        // console.log(`Response ${response}`)
        alert(data)
        // Update the HTML content of the summary div with the fetched data
        summaryDiv.innerText = data;

});
}
