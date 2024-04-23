const userInfo = localStorage.getItem("user_login");
const username = localStorage.getItem("username");

let isLoggedIn = userInfo ? true : false;
const login = document.getElementsByClassName("login")[0];
const register = document.getElementsByClassName("register")[0];
const Logout = document.getElementsByClassName("logout")[0];
const content = document.getElementsByClassName("content")[0];
const main = document.getElementById("main-app");
const navUsername = document.getElementsByClassName("usernameNav")[0];
const subarea = document.getElementById("subarea");

const serverURL = ""
const apiKey = "";

const sub = () => {
  buildHTML = "";
  axios
    .post(
      serverURL + "/getSubSongs",
      {
        headers: { "Access-Control-Allow-Origin": "*" },
        useremail: userInfo,
      },
      {
        headers: {
          "x-api-key": apiKey,
        },
      }
    )
    .then((response) => {
      let data = response.data;
      console.log(data);
      for (let i = 0; i < data.length; i++) {
        let artist = data[i].artist;
        let title = data[i].title;
        buildHTML += `<div class="row text data" id="sub_${data[i].artist}-${data[i].title}">
            <div class="col">${data[i].artist}</div>
            <div class="col">${data[i].title}</div>
            <div class="col">${data[i].year}</div>
            <div class="col"><img src="${data[i].img_url}" height="250px" width="250px"></div>
            <button type="button" onclick="handleRemove()" class="col btn btn-outline-danger" id="sub-${data[i].artist}-${data[i].title}" style="height:20%">Remove</button>
            </div>`;
      }
      document.getElementById("sub-body").innerHTML = buildHTML;
    })
    .catch((err) => {
      console.log(err);
    });
};
sub();

const handleRemove = () => {
  let artist = event.target.id.split("-")[1];
  console.log(artist);
  let title = event.target.id.split("-")[2];
  console.log(title);
  console.log(userInfo);
  const config = {
    headers: {
      'x-api-key': apiKey 
    },
    data: {
        email: userInfo,
        artist: artist,
        title: title,
      } 
  };
  axios
    .delete(
      "",
      config
    )
    .then((response) => {
      console.log(response);
      if (response.data.statusCode != 400) {
        alert("Sucessfully unsubscribed");
      }
    })
    .catch((err) => {
      console.log(err);
    });
  //update search
  Search("noalert");
  console.log(event.target.parentNode.remove());
};

if (isLoggedIn) {
  login.style.display = "none";
  register.style.display = "none";
  Logout.style.display = "block";
  content.style.display = "none";
  main.style.display = "block";
  navUsername.textContent = username;
  subarea.style.display = "block";
}

const logout = () => {
  isLoggedIn = false;
  localStorage.removeItem("user_login");
  localStorage.removeItem("username");
  content.textContent = "Logged Out";
};

const Search = (alertstatus) => {
  const title = document.getElementById("title-input").value.trim();
  const artist = document.getElementById("artist-input").value.trim();
  const year = document.getElementById("year-input").value.trim();
  if (alertstatus !== "noalert") {
    if (!title && !artist && !year) {
      return alert("No result is retrieved. Please query again");
    }
  }
  const result = { title: title, artist: artist, year: year };
  axios
    .post(
      serverURL + "/query-songs",
      {
        headers: { "Access-Control-Allow-Origin": "*" },
        title: title,
        artist: artist,
        year: year,
      },
      {
        headers: {
          "x-api-key": apiKey,
        },
      }
    )
    .then((response) => {
      if (response.data.length == 0) {
        return alertstatus != "noalert"
          ? alert("No result is retrieved. Please query again")
          : "";
      }
      showQuery(response.data);
      console.log(response.data);
    })
    .catch((err) => {
      console.log(err);
    });
};

const showQuery = (data) => {
  let buildHTML = "";
  for (let i = 0; i < data.length; i++) {
    let checkat = data[i].artist;
    let checktt = data[i].title;
    let checkId = document.getElementById("sub-" + checkat + "-" + checktt);
    //disabled button if the id is found
    if (checkId) {
      buildHTML += ` <tr>
        <th scope="row">${data[i].artist}</th>
        <td>${data[i].title}</td>
        <td>${data[i].year}</td>
        <td><img src="${data[i].img_url}" height="250px" width="250px"></td>
        <td><button onclick="handleSub()" class="btn btn-success disabled" id="${data[i].artist}*${data[i].title}">
        Subscribe</button>
        <p>You subscribed to this song</p>
        </td>
      </tr>`;
    } else {
      buildHTML += ` <tr>
        <th scope="row">${data[i].artist}</th>
        <td>${data[i].title}</td>
        <td>${data[i].year}</td>
        <td><img src="${data[i].img_url}" height="250px" width="250px"></td>
        <td><button onclick="handleSub()" class="btn btn-success" id="${data[i].artist}*${data[i].title}">Subscribe</button></td>
      </tr>`;
    }
  }
  document.getElementById("tbody").innerHTML = buildHTML;
};

const handleSub = () => {
  event.preventDefault();
  event.target.classList.add("disabled");
  data = event.target.id.split("*");
  let p = document.createElement("p");
  let button = event.target;
  p.textContent = "You subscribed to this song";
  button.parentNode.insertBefore(p, button.nextSibling);
  axios
    .post(
      serverURL + "/subsong",
      {
        headers: { "Access-Control-Allow-Origin": "*" },
        email: userInfo,
        artist: data[0],
        title: data[1],
      },
      {
        headers: {
          "x-api-key": apiKey,
        },
      }
    )
    .then((response) => {
      console.log(response.data);
      if (response.data.statusCode != 400) {
        alert("Sucessfully subscribed");
      }
      sub();
    })
    .catch((err) => {
      console.log(err);
    });
};
