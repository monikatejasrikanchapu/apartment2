function speak(text) {
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(text);
        window.speechSynthesis.speak(utterance);
    }
}

function clearHighlights() {
    document.querySelectorAll('.flat').forEach(el => el.classList.remove('highlight'));
}

function highlightFlat(flatNum) {
    clearHighlights();
    // Find which flat it is
    const lastDigit = flatNum.charAt(2); // Assuming flatNum is like 101, 202
    let flatId = "";

    if (lastDigit === '1') flatId = "flatA";
    else if (lastDigit === '2') flatId = "flatB";
    else if (lastDigit === '3') flatId = "flatC";

    if (flatId) {
        document.getElementById(flatId).classList.add('highlight');
    }
}

function updateFlatLabels(floor) {
    const flatA = document.getElementById("flatA");
    const flatB = document.getElementById("flatB");
    const flatC = document.getElementById("flatC");

    flatA.innerText = `${floor}01`;
    flatB.innerText = `${floor}02`;
    flatC.innerText = `${floor}03`;
}

function askChatbot() {
    const flatInput = document.getElementById('flatInput').value.trim();
    if (!flatInput || isNaN(flatInput) || flatInput.length !== 3) {
        alert("Please enter a valid flat number like 101, 202, etc.");
        return;
    }

    fetch('/get_flat_info', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ flat_number: flatInput })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('chatbotResponse').innerText = data.message;

        // Update dynamic flat labels
        const floor = flatInput.charAt(0);
        updateFlatLabels(floor);

        // Highlight and speak
        highlightFlat(flatInput);
        speak(data.message);
    });
}
