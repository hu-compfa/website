var checkboxes = document.querySelectorAll(".videos-container ul li input");
var selectVideos = document.querySelector("#checkbox");
selectVideos.addEventListener("change", function() {
  
  for (let index = 0; index < checkboxes.length; index++) {
    if (this.checked) {
 
      checkboxes[index].style.display = "block" ;
      document.querySelector(".select-all").style.display = "inline"
    }
    else {
      checkboxes[index].style.display = "none";
      document.querySelector(".select-all").style.display = "none";
    }  
}
})
var links = document.getElementsByClassName("video-link");
var linksList = []
for (var i  = 0; i  < checkboxes.length; i ++) {
  checkboxes[i].index = i
  checkboxes[i].addEventListener("change", function() {
    
    if (this.checked) {
      linksList.push(links[this.index])
      
    }else {
      var deleteElement = linksList.indexOf(links[this.index])
      linksList.splice(deleteElement, 1);
      
    }
  })
}



document.getElementById("downloadAllVideos").addEventListener("click", function() {
  for (let i = 0; i < linksList.length; i++) { 
      linksList[i].click();
  }
})

document.querySelector(".select-all input").addEventListener("change", function() {
  for (let i = 0; i < checkboxes.length; i++) {
    if (this.checked) {
      
      checkboxes[i].click()
    }else {
      checkboxes[i].click()
      
    }

  }

})