//sidebar function

var sidebar = document.getElementById("sidebar")

function opennav(){
    var body = document.querySelector("body");
    body.style.overflow =  "hidden"    
    sidebar.style.display = "block";

}

function closenav(){
    var body = document.querySelector("body");
    sidebar.style.display = "none";
    body.style.overflow =  "scroll"
}


//end

//navbar scroll function

var scrollFunction = function(){

    var navBar = document.getElementsByTagName("nav")[0];
    var hideBtn =  document.getElementsByClassName("hide");

 
    var y = window.scrollY;
    if (y > 2){
        navBar.classList.add("nav-bg")
        for (i=0;i<2;i++){
            hideBtn[i].style.visibility = "visible"

        }
    }
    else{
        navBar.classList.remove("nav-bg")
        for (i=0;i<2;i++){
            hideBtn[i].style.visibility = "hidden"
        }
    }
}
window.addEventListener("scroll",scrollFunction)


//video banner

var vid = document.getElementById("vid")
var videoDiv = document.getElementById("features")

window.addEventListener("scroll",()=>{
    if (isInViewport(vid)){
        vid.play();
    }
    else{
        vid.pause();
    }
})

function isInViewport(element) {
    var rect = element.getBoundingClientRect();
    return (
      rect.top >= 0 &&
      rect.left >= 0 &&
      rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
      rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
  }

  function changevid1(){
    var vidDiv = document.getElementById("vid-div")
    vidDiv.scrollTo(0,0)
    var vidDiv2 = document.getElementById("vid-div2")
    vidDiv2.scrollTo(0,0)
    var vidDiv3 = document.getElementById("vid-div3")
    vidDiv3.scrollTo(0,0)
  }
  function changevid2(){
    var vidDiv = document.getElementById("vid-div")
    vidDiv.scrollTo(0,635)
    var vidDiv2 = document.getElementById("vid-div2")
    vidDiv2.scrollTo(0,635)
    var vidDiv3 = document.getElementById("vid-div3")
    vidDiv3.scrollTo(0,635)
    
  }
  function changevid3(){
    var vidDiv = document.getElementById("vid-div")
    vidDiv.scrollTo(0,1270)
    var vidDiv2 = document.getElementById("vid-div2")
    vidDiv2.scrollTo(0,1270)
    var vidDiv3 = document.getElementById("vid-div3")
    vidDiv3.scrollTo(0,1270)
  }