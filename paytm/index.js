const ua = navigator.userAgent;
console.log(ua);    
if (ua.match(/iPhone|Android/i)){
    document.getElementById("pc").style.display = "none";
    document.getElementById("mobile").style.display = "block"

}
else{
    document.getElementById("mobile").style.display = "none";
    document.getElementById("pc").style.display = "block"  
}

function hideSignin(){
    document.getElementById("mobileSignIn").classList.toggle("hide-btn")
}

document.getElementById("sidebarToggle").addEventListener("click",hideSignin())