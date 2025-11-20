document.addEventListener("DOMContentLoaded", () => {

    const sendButton = document.getElementById("send-button");
    const micButton = document.getElementById("mic-button");
    const pauseButton = document.getElementById("pause-button");
    const userInput = document.getElementById("user-input");
    const chatWindow = document.getElementById("chat-window");
    const statusDisplay = document.getElementById("status-display");
    const stickerContainer = document.getElementById("ai-sticker-container");

    let recognition = null;

    // STATUS
    function setStatus(text, show = true) {
        statusDisplay.textContent = text;
        statusDisplay.style.display = show ? "block" : "none";
    }

    // STICKER
    function showSticker(show = true) {
        stickerContainer.style.display = show ? "block" : "none";
    }

    // Add message box
    function addMessage(text, sender) {
        const msg = document.createElement("div");
        msg.classList.add("message", sender === "user" ? "user-message" : "ai-message");
        msg.textContent = text;
        chatWindow.appendChild(msg);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // TTS (pause fixed)
    function speak(text) {
        try {
            window.speechSynthesis.cancel();

            const utter = new SpeechSynthesisUtterance(text);
            utter.lang = "mr-IN";

            window.speechSynthesis.speak(utter);

            pauseButton.disabled = false;
            pauseButton.textContent = "⏸️";

            utter.onend = () => {
                pauseButton.disabled = true;
            };

        } catch (err) {
            console.warn("TTS error:", err);
        }
    }

    // SIMPLE API CALL
    async function callAPI(query) {
        const body = {
            query: query,
            lang: /[\u0900-\u097F]/.test(query) ? "mr" : "en"
        };

        const res = await fetch("/public/query", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body)
        });

        return await res.json();
    }

    function setLoading(isLoading) {
        sendButton.disabled = isLoading;
        micButton.disabled = isLoading;
        userInput.disabled = isLoading;
        if (!isLoading) pauseButton.disabled = false;
    }

    async function sendMessage() {
        const text = userInput.value.trim();
        if (!text) return;

        addMessage(text, "user");
        userInput.value = "";

        setLoading(true);
        setStatus("⏳ शोधत आहे...");
        showSticker(true);

        const response = await callAPI(text);

        addMessage(response.answer, "ai");
        speak(response.answer);

        setStatus("🔊 बोलत आहे...");
        showSticker(false);
        setLoading(false);
    }

    sendButton.addEventListener("click", sendMessage);

    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") sendMessage();
    });

    // PAUSE BUTTON FIX
    pauseButton.addEventListener("click", () => {
        if (!window.speechSynthesis.speaking) return;

        if (window.speechSynthesis.paused) {
            window.speechSynthesis.resume();
            pauseButton.textContent = "⏸️";
        } else {
            window.speechSynthesis.pause();
            pauseButton.textContent = "▶️";
        }
    });

    // MICROPHONE
    if ("webkitSpeechRecognition" in window) {
        recognition = new webkitSpeechRecognition();
        recognition.lang = "mr-IN";

        recognition.onresult = async (event) => {
            const spoken = event.results[0][0].transcript;
            addMessage(spoken, "user");

            const response = await callAPI(spoken);
            addMessage(response.answer, "ai");
            speak(response.answer);
        };

        micButton.onclick = () => recognition.start();
    }

    setStatus("🟢 तयार.");
});
