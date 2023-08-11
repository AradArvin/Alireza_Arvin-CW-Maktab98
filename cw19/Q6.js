// 6.

let firstName = "arad"
let lastName = "arvin"
let age = 28
let country = "iran"
let city = "shahindej"

let info = {
    "firstname":firstName,
    "lastname":lastName,
    "age":age,
    "country":country,
    "city":city
}

let strinfo = JSON.stringify(info)

localStorage.setItem("info", strinfo)
