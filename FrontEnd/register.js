const serverURL = "";
const form = document.getElementById("registerForm")
let email = document.getElementById("email");
let username = document.getElementById("username");
let password = document.getElementById("password");
const apiKey = ""

form.addEventListener("submit",(e) => {
    e.preventDefault();
    if (!email.value || !username.value || !password.value) {
        alert("Please fill all inputs");
        return
    }
    console.log(email.value) 
    console.log(password.value) 
    axios.post(serverURL, {
        headers: {"Access-Control-Allow-Origin": "*"},
        email: email.value,
        password: password.value,
        username: username.value,
        type:"add"
      },{headers:{
        'x-api-key':apiKey
      }})
      .then((response) => {
        console.log(response)
        if (response.data.statusCode != 201) {
            alert("The email already exists");
            return
        } else {
            setTimeout(() => {
            alert("Register Successfully!");
            window.location.replace("/login.html");
            });
        }
        console.log(response);
      })
      .catch((err) => {
        alert("The email already exists");
      });
})

//to do https://zetcode.com/javascript/axios/

