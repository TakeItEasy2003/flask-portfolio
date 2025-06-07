// Animate content on load
document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll("main > *");
    items.forEach((el, i) => {
        el.style.opacity = 0;
        el.style.transform = "translateY(20px)";
        setTimeout(() => {
            el.style.transition = "all 0.6s ease";
            el.style.opacity = 1;
            el.style.transform = "translateY(0)";
        }, i * 150);
    });
});

// Form alert (placeholder functionality)
const form = document.querySelector("form");
if (form) {
    form.addEventListener("submit", function (e) {
        alert("Thanks! Your message was submitted.");
    });
}

document.addEventListener("keydown", function (event) {
    if (event.shiftKey && event.key === "A") {
        window.location.href = "/admin-login";
    }
});
