

const el = document.querySelector("body");

el.addEventListener("mousemove", (e) => {
  el.style.backgroundPositionX = (-e.offsetX*0.01) + "px";
  el.style.backgroundPositionY = (-e.offsetY*0.01) + "px";
});


const nav = document.querySelector(".nav")
const menuBtn = document.querySelector(".menu-btn")
const menulist = document.querySelector(".nav-list")
menuBtn.addEventListener("click",()=>{
  nav.classList.toggle("open")
  menulist.classList.toggle("open")
})