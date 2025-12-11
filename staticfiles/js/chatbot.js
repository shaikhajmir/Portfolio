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

  if (toggle) {
    toggle.addEventListener("click", () => {
      box.classList.toggle("hidden");
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener("click", () => {
      box.classList.add("hidden");
    });
  }

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const text = btn.innerText.trim();
      addMessage(text, false);

      if (text === "Show skills") {
        addMessage("Shaikh works with Python, Django, Flask, PHP, MySQL, Android, HTML, CSS, JavaScript, Git/GitHub, deployment and more.");
      } else if (text === "Show projects") {
        addMessage("Check out the Projects page to see weather app, AI drawing game, image compressor, safe home system and more.");
      } else if (text === "Contact info") {
        addMessage("You can contact Shaikh via the Contact page or email (update in template): your-email@example.com");
      } else if (text === "Current learning") {
        addMessage("Currently learning advanced Django, REST APIs, deployment, and cloud fundamentals.");
      }
    });
  });
});
