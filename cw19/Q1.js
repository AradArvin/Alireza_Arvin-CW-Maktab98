
// 1.

let input;

document.getElementById("subbtn").onclick = function(){

    input = document.getElementById("inputField").value;
    if(parseInt(input,10)){
        alert("The type of input is Number");
    }
    else if(isNaN(input)){
        alert("The type of input is String");
    }
    
}