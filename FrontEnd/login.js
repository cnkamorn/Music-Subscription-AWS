const serverURL = ""
const apiKey = "";

const checkLogin = (event) => {
  event.preventDefault();
  let email = document.getElementById("email");
  let password = document.getElementById("password");
  if (!email.value || !password.value) {
    return;
  }
  axios
    .post(
      serverURL,
      {
        email: email.value,
        password: password.value,
      },
      {
        headers: {
          "x-api-key": apiKey,
        },
      }
    )
    .then((response) => {
      if (response.data.statusCode != 200) {
        throw "password incorrect";
      }
      localStorage.setItem("user_login", email.value);
      localStorage.setItem("username", response.data.body.username);
      console.log(response);
      setTimeout(() => {
        window.location.replace("/");
      }, 1500);
      console.log(response);
    })
    .catch((err) => {
      console.log(err);
      alert("email or password is invalid");
    });
  console.log(email.value, password.value);
};
