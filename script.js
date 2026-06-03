const entireScreen = document.getElementById('entireScreen');

let mouseX = 0;
let mouseY = 0;
let gradientSize = '600px';
let gradientColor = '#FFFFFF';
let gradientTransparancy = 'transparent 80%';

function updateGradient() {
  const xPos = mouseX + window.scrollX;
  const yPos = mouseY + window.scrollY;
  entireScreen.style.background = `radial-gradient(${gradientSize} at ${xPos}px ${yPos}px, ${gradientColor}, ${gradientTransparancy})`;
}

window.addEventListener("mousemove", (e) => {
  mouseX = e.clientX;
  mouseY = e.clientY;
  updateGradient();
  
});


window.addEventListener("scroll", () => {
  updateGradient();
});