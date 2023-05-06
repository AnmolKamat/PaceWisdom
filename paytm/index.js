const ua = navigator.userAgent;
console.log(ua);    
if (ua.match(/iPhone|Android/i)){
    document.getElementById("pc").style.display = "none";
    document.getElementById("mobile").style.display = "block"
}

