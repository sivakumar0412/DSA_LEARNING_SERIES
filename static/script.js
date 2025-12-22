window.onload = function () {
    const theme = localStorage.getItem("theme");
    const toggle = document.getElementById("themeToggle");

    if (theme === "dark") {
        document.body.classList.add("dark-mode");
        toggle.checked = true;
    }

    // Trigger confetti if result exists
    if (document.querySelector(".result")) {
        launchConfetti();
    }
};

function toggleTheme() {
    const toggle = document.getElementById("themeToggle");

    if (toggle.checked) {
        document.body.classList.add("dark-mode");
        localStorage.setItem("theme", "dark");
    } else {
        document.body.classList.remove("dark-mode");
        localStorage.setItem("theme", "light");
    }
}

/* 🎉 Confetti Logic */
function launchConfetti() {
    const container = document.getElementById("confetti-container");
    const colors = ["#ff0a54", "#ff477e", "#ff85a1", "#ffd166", "#06d6a0"];

    for (let i = 0; i < 80; i++) {
        const confetti = document.createElement("div");
        confetti.classList.add("confetti");

        confetti.style.left = Math.random() * 100 + "vw";
        confetti.style.backgroundColor =
            colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDuration = 2 + Math.random() * 2 + "s";

        container.appendChild(confetti);

        // Remove after animation
        setTimeout(() => {
            confetti.remove();
        }, 4000);
    }
}
