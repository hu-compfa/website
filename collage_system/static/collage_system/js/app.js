$(document).ready(function() {
    $(".login-container a").click(function() {
      $(".login-dropdown").slideToggle(200)
    })
    $(document).click(function(event) {
      if (!event.target.matches(".login-dropdown") && !event.target.matches(".login-container a") && !event.target.matches("input") && !event.target.matches("svg") && !event.target.matches("svg path")) {
        $(".login-dropdown").slideUp(200)
      }
      
    })
})

// Toggle Form In One Page 
var addItems = document.querySelectorAll(".add-items-bar");
var contentsDisplay = document.querySelectorAll(".adding-contents")
for (var i = 0; i < addItems.length; i++) {
  addItems[i].index = i
  addItems[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active-li-a");
    var currentContent = document.getElementsByClassName("displayAdding");
    current[0].classList.remove("active-li-a");
    currentContent[0].classList.remove("displayAdding");
    this.classList.add("active-li-a");
    var newIndext = this.index;
    contentsDisplay[newIndext].classList.add("displayAdding")
     
    // contentsDisplay[newIndex].classList.add("displayAdding")
  })
}

// function changeContents() {
//   var current = document.getElementsByClassName("active-li-a");
//   current[0].classList.remove("active-li-a");

//   addItems[0].classList.add('active-li-a');
// }


var navbarsContainer = document.querySelector(".navbar-container")

// var addCourseButton = document.getElementById("add-course-button")






// // Event Leasiner


navbarsContainer.addEventListener("click" , toggelNavbars)




// functions 

function toggelNavbars(){
    if (!navbarsContainer.classList.contains("close")) {
        navbarsContainer.classList.add("close")
        document.querySelector("nav").classList.add("displayingNav");
        document.querySelector("nav").classList.remove("hiddeingNav");
        document.querySelector(".background-black").classList.add("displayingNav")
        document.querySelector(".background-black").classList.remove("hiddeingNav")
        document.querySelector("body").style.overflowY = "hidden";
        
       
        
    }
    else {
        navbarsContainer.classList.remove("close")
        document.querySelector("nav").classList.add("hiddeingNav");
        document.querySelector("nav").classList.remove("displayingNav")
        document.querySelector(".background-black").classList.add("hiddeingNav");
        document.querySelector(".background-black").classList.remove("displayingNav");
        document.querySelector("body").style.overflowY = ""
        
    }
    
}
window.onclick = function(event) {
    if(event.target.matches(".background-black")) {
        console.log("NAV Cacth")
        navbarsContainer.classList.remove("close")
        document.querySelector("nav").classList.add("hiddeingNav");
        document.querySelector("nav").classList.remove("displayingNav")
        document.querySelector("body").style.overflowY = ""
        document.querySelector(".background-black").classList.add("hiddeingNav")
        document.querySelector(".background-black").classList.remove("displayingNav")
       
    }
}

// // Control Panel Page 



// Download All Videos

// var downloadAllVideos = document.getElementById("downloadAllVideos")
// var aTargets = document.querySelectorAll(".videos-container ul li a");
// var videosLink =  [];
// for (let index = 0; index < aTargets.length; index++) {
//   videosLink.push(aTargets[index].getAttribute("href"))
// }



// downloadAllVideos.addEventListener("click", function(event) {
//   var zip = new JSZip();
//   for (let index = 0; index < videosLink.length; index++) {
//     console.log(videosLink)
        
//     var videos = zip.folder("videos");
//     console.log(videos)
//     videos.file("10.mp4"+".mp4", {base64: true});
    
//     zip.generateAsync({type:"base64"}).then(function(content) {
//         // see FileSaver.js
//         saveAs(content, "Tutorail_Videos.zip");
//     });
    
//   }
// })