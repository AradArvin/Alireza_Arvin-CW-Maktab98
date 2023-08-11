// 2.

let age;

document.getElementById("subbtn").onclick = function(){

    age = document.getElementById("inputField").value;
    let nAge = Number(age); 
    if(nAge >= 0 && nAge <= 10){
        console.log("child")
    }
    else if(nAge >= 11 && nAge <= 18){
        console.log("teenager")
    }
    else if(nAge >=19 && nAge <= 30){
        console.log("young person")
    }
    else if(nAge > 30){
        console.log("adult")
    }
    else{
        console.log("invalid age")
    }

}