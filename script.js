let entireScreen = document.getElementById('entireScreen');

window.addEventListener("mousemove", (e) => {
  let xPos = e.clientX;
  let yPos = e.clientY;
  let size = '600px'
  let color = '#FFFFFF'
  
  let transparency = 'transparent 90%';

  entireScreen.style.background = `radial-gradient( 600px at ${xPos}px ${yPos}px, ${color}, ${transparency})`;
  
});