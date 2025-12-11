document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("chatbot-toggle");
  const box = document.getElementById("chatbot-box");
  const closeBtn = document.getElementById("chatbot-close");
  const msgContainer = document.getElementById("chatbot-messages");
  const buttons = document.querySelectorAll(".chatbot-btn");

  function addMessage(text, fromBot = true) {
    const div = document.createElement("div");
    div.className = `rounded-xl px-3 py-2 w-fit max-w-[90%] mb-1 text-xs ${
      fromBot ? "bg-slate-800" : "bg-indigo-500 self-end ml-auto"
    }`;
    div.innerText = text;
    msgContainer.appendChild(div);
    msgContainer.scrollTop = msgContainer.scrollHeight;
  }

  function openChat() {
    box.classList.remove("hidden");
    // small timeout so CSS transition works
    setTimeout(() => {
      box.classList.add("chatbot-open");
    }, 10);
  }

  function closeChat() {
    box.classList.remove("chatbot-open");
    setTimeout(() => {
      box.classList.add("hidden");
    }, 180); // match CSS transition time
  }

  if (toggle) {
    toggle.addEventListener("click", () => {
      const isHidden = box.classList.contains("hidden");
      if (isHidden) {
        openChat();
      } else {
        closeChat();
      }
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener("click", () => {
      closeChat();
    });
  }

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const text = btn.innerText.trim();
      addMessage(text, false);

      if (text === "Show skills") {
        // You can also navigate to the languages page (added below)
        addMessage("I work with multiple languages like Python, JavaScript, PHP, MySQL, Android and more. Check the Languages page for full list.");
      } else if (text === "Show projects") {
        addMessage("Check out the Projects page to see weather app, AI drawing app, image compressor, safe home system and more.");
      } else if (text === "Contact info") {
        addMessage("You can contact Shaikh anytime at: shaikhajmirilal8@gmail.com");
      } else if (text === "Current learning") {
        addMessage("Currently learning advanced Django, REST APIs, deployment, and cloud fundamentals.");
      }
    });
  });
});
