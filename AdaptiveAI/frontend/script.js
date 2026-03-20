const sections = document.querySelectorAll("section");

window.addEventListener("scroll", () => {
sections.forEach(sec => {
if (sec.getBoundingClientRect().top < window.innerHeight - 100) {
sec.classList.add("show");
}
});
});

/* TYPING EFFECT */
let text = "Analyzing Resume → Mapping Skills → Generating AI Roadmap...";
let i = 0;

(function typing() {
if (i < text.length) {
document.getElementById("typing").innerHTML += text.charAt(i);
i++;
setTimeout(typing, 30);
}
})();

/* SKILL ANIMATION */
const fills = document.querySelectorAll(".fill");

window.addEventListener("scroll", () => {
fills.forEach(f => {
if (f.getBoundingClientRect().top < window.innerHeight) {
f.style.width = f.dataset.width;
}
});
});
document.getElementById("extractBtn").addEventListener("click", async () => {

    let text = document.getElementById("resumeInput").value;

    const res = await fetch(`${API}/extract-skills`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });

    const data = await res.json();

    document.getElementById("output").innerHTML = JSON.stringify(data);

});

async function testBackend() {
    try {
        const res = await fetch("https://adaptive-backend.onrender.com/");
        const data = await res.json();

        console.log(data);

        document.body.innerHTML += `<p>${data.message}</p>`;
    } catch (err) {
        console.error(err);
    }
}

testBackend();
async function uploadResume() {
    const file = document.getElementById("resumeFile").files[0];

    let formData = new FormData();
    formData.append("file", file);

    const res = await fetch("https://adaptive-backend.onrender.com/upload", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    console.log(data);
}

/* TIMELINE LOOP */
let steps = document.querySelectorAll(".step");
let idx = 0;

setInterval(() => {
steps.forEach(s => s.classList.remove("active"));
steps[idx].classList.add("active");
idx = (idx + 1) % steps.length;
}, 1400);

/* API CALL */
async function callAPI() {
try {
const response = await fetch("https://adaptive-ai.onrender.com/api");
const data = await response.json();
console.log(data);

document.body.innerHTML += `<p>${data.message}</p>`;
} catch (error) {
console.error("Error:", error);
}
}

callAPI();