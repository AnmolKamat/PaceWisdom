let bd =  document.getElementById("particle-container")

// for (let i=0;i<50;i++){
//     let emoji = document.createElement("h6")
//     emoji.innerHTML = "🏀"
//     emoji.style.position = "absolute"
//     emoji.classList.add("bg-emo")
//     
//     emoji.style.top = Math.floor(Math.random()*70)+"%"
//     emoji.style.left = Math.floor(Math.random()*100)+"%"
//     bd.appendChild(emoji)
// }


for (let i=0;i<50;i++){
    let particle = document.createElement("div")
    particle.classList.add("particle")
    particle.innerHTML = "🐶"
    bd.appendChild(particle)
}