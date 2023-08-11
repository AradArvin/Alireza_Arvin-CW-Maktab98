//  7.

let firstName = "student1"
let lastName = "study"
let age = 15
let skills = "cooking"
let country = "uganda"
let enrolled = "highschool"

let student = {
    "firstname":firstName,
    "lastname":lastName,
    "age":age,
    "skills":skills,
    "country":country,
    "enrolled":enrolled
}


let strstudent = JSON.stringify(student)

localStorage.setItem(strstudent)