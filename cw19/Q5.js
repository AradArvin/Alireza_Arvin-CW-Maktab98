// 5.


function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
  }
  
  function getCookie(cname) {
    let name = cname + "=";
    let ca = document.cookie.split(';');
    for(let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }



function getDateString(expirayDate=0) {
    const date = new Date();
    date.setDate(date.getDate() + expirayDate);
    return date.toUTCString();
}


function saveUserName(){
    let check = document.getElementById("chBox").checked
    console.log(check)
    if (check){
        let username = document.getElementById("userField").value
        let password = document.getElementById("passField").value
        setCookie("username", username, 7)
        setCookie("password", password, 7)
    }
}

function getData(){
    if (getCookie("username") !== ""){
        document.getElementById("userField").value = getCookie("username")
        document.getElementById("passField").value = getCookie("password")
    }
}

document.addEventListener("DOMContentLoaded", getData);
