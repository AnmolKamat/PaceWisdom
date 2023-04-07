const h=getElement = (selector)=>{
  const element = document.querySelector(selector)
  if(element) return element
}

const links = getElement(".nav-links")
const navbtn = getElement(".nav-btn")

navbtn.addEventListener("click",()=>{
  links.classList.toggle("show-links")
})

const date = getElement("#date")
const currYear = new Date().getFullYear()
date.textContent = currYear