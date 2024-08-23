const chatbotToggler = document.querySelector(".chatbot-toggler");
const closeBtn = document.querySelector(".close-btn");
const chatbox = document.querySelector(".chatbox");
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");

let userMessage = null;
const API_KEY = "PASTE-YOUR-API-KEY"; 
const inputInitHeight = chatInput.scrollHeight;

const createChatLi = (message, className) => {
    
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", `${className}`);
    let chatContent = className === "outgoing" ? `<p></p>` : `<span class="material-symbols-outlined">smart_toy</span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi; 
}

const generateResponse = (chatElement) => {
    const API_URL = "https://api.openai.com/v1/chat/completions";
    const messageElement = chatElement.querySelector("p");

    
    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${API_KEY}`
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{role: "user", content: userMessage}],
        })
    }

  fetch(API_URL, requestOptions)
        .then(res => res.json())
        .then(data => {
        
            const userMessageLower = userMessage.toLowerCase();
            let responseMessage = "I'm sorry, I didn't understand that.";

            // Chat bot responses
            if (userMessageLower.includes("hello") || userMessageLower.includes("hi")) {
                responseMessage = "Hello! How can I assist you today?";
            }
            if (userMessageLower.includes("agrisage") || userMessageLower.includes("about")) {
                responseMessage = "AgriSage transforms paddy farming with advanced technology like deep learning, IoT, and personalized fertilizer recommendations, enhancing management practices.";
            } 
            else if (userMessageLower.includes("iot") || userMessageLower.includes("real-time")) {
                responseMessage = "AgriSage offers IoT sensors in paddy fields to collect real-time data on soil moisture, temperature, and more. This data is presented on a centralized dashboard for farmers to monitor, enabling them to receive alerts for proactive interventions.";
            } 
            else if (userMessageLower.includes("fertilizers") || userMessageLower.includes("recommendations")) {
                responseMessage = "AgriSage provides an intelligent system that recommends specific fertilizers based on identified diseases in paddy fields. AgriSage considers factors such as soil composition, weather conditions, and the type of disease to tailor fertilizer recommendations. Farmers receive clear and actionable plans for applying recommended fertilizers, aiming to optimize crop health and yield.";
            } 
            else if (userMessageLower.includes("disease") || userMessageLower.includes("management")) {
                responseMessage = "AgriSage implements deep learning models to analyze images of paddy fields, identifying diseases promptly. Farmers can upload images via a user-friendly interface for disease classification. Detailed disease information and actionable solutions are provided to mitigate their impact.";
            } 
            else if (userMessageLower.includes("chat-bot") || userMessageLower.includes("personalized assistance")) {
                responseMessage = "AgriSage integrates a chat-bot into its web application to provide instant and personalized assistance to farmers. The chat-bot answers queries on disease identification, field monitoring, fertilizer recommendations, and general farming practices, enhancing farmer support and efficiency.";
            } 



            messageElement.textContent = responseMessage;
        })
        .catch(() => {
            messageElement.classList.add("error");
            messageElement.textContent = "Error! Something went wrong. Please try again.";
        })
        .finally(() => chatbox.scrollTo(0, chatbox.scrollHeight));
}

const handleChat = () => {
    userMessage = chatInput.value.trim(); 
    if(!userMessage) return;

    
    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;

    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);
    
    setTimeout(() => {
        
        const incomingChatLi = createChatLi("Thinking...", "incoming");
        chatbox.appendChild(incomingChatLi);
        chatbox.scrollTo(0, chatbox.scrollHeight);
        generateResponse(incomingChatLi);
    }, 600);
}

chatInput.addEventListener("input", () => {
    
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
   
    if(e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
});

sendChatBtn.addEventListener("click", handleChat);
closeBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));