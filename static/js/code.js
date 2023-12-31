// GLOBAL VARIABLES
let USERNAME = ""
let PASSWORD = ""
let LIST_NOTES_OBJ = [];
const div_user_in = document.getElementById('user_in');
const div_user_out = document.getElementById('user_out');
const div_display_user = document.getElementById('display_username');
const in_username = document.getElementById('username');
const in_password = document.getElementById('password');

// DONE
function user_login() {
    const username = in_username.value;
    const password = in_password.value;
    const data = { username, password }
    axios.post('/api/user/login', data)
        .then(function (response) {
            const msg = response.data.msg;
            if (msg === "SUCCESS") {
                localStorage.setItem("username", username);
                localStorage.setItem("password", password);
                USERNAME = username;
                PASSWORD = password;
                render_in();
                notes_get_all();
            } else if (msg = "USER_INVALID") {
                document.getElementById("error-msg").innerText = "INVALID CREDENTIALS";
            }
        })
        .catch(function (error) {
            console.error('Error');
            document.getElementById("error-msg").innerText = "INVALID CREDENTIALS";
        });
}

// DONE
function user_register() {
    const username = in_username.value;
    const password = in_password.value;
    const data = { username, password }
    axios.post('/api/user/register', data)
        .then(function (response) {
            const msg = response.data.msg;
            if (msg === "SUCCESS") {
                localStorage.setItem("username", username);
                localStorage.setItem("password", password);
                USERNAME = username;
                PASSWORD = password;
                render_in();
            } else if (msg === "USER_EXISTS") {
                document.getElementById("error-msg").innerText = "USER ALREADY EXISTS";
            }
        })
        .catch(function (error) {
            console.error('Error');
        });
}
// DONE
function user_logout() {
    localStorage.removeItem("username")
    localStorage.removeItem("password")
    USERNAME = null;
    PASSWORD = null;
    // render_out();
    location.reload();
}

function notes_get_all() {
    const data = { username: localStorage.getItem('username'), password: localStorage.getItem('password') }
    const end_point = '/api/notes/read'
    axios.post(end_point, data)
        .then(function (response) {
            const msg = response.data.msg;
            const data = response.data.data;
            let html_str = ""
            for (let i = 0; i < data.length; i++) {
                html_str += `<div style="padding: 10px; background-color:#fff5; position: relative;" class="notes-item">
                ${marked(data[i]['content'])}
                <div style="position: absolute;top: 0px;right:0px;display: flex;gap:0px;" id="options">
                    <button onclick="notes_delete(${data[i]["id"]})">Delete</button>
                </div>
            </div>`
            }
            document.getElementById("left-main").innerHTML = html_str;
        })
        .catch(function (error) {
            console.error('Error');
        });
}
// DONE
function notes_create() {
    const data = {
        username: localStorage.getItem('username'),
        password: localStorage.getItem('password'),
        content: document.getElementById("content").value
    }
    const end_point = '/api/notes/create'
    axios.post(end_point, data)
        .then(function (response) {
            const msg = response.data.msg;
            if (msg == "SUCCESS") {
                notes_get_all();
                document.getElementById("content").value = "";
            }
        })
        .catch(function (error) {
            console.error('Error');
        });
}
function notes_delete(id) {
    const data = {
        username: localStorage.getItem('username'),
        password: localStorage.getItem('password'),
        id,
    }
    const end_point = '/api/notes/delete'
    axios.post(end_point, data)
        .then(function (response) {
            const msg = response.data.msg;
            notes_get_all();
        })
        .catch(function (error) {
            console.error('Error');
        });
}


// USER COMPONENT
function render_in() {
    console.log("USER IN");
    div_display_user.innerText = localStorage.getItem("username");
    div_user_in.style.display = 'flex';
    div_user_out.style.display = 'none';

}

function render_out() {
    console.log("USER OUT");
    div_user_in.style.display = 'none';
    div_user_out.style.display = 'flex';
}


window.onload = function () {
    if (localStorage.getItem('username') === null) {
        render_out();
    } else {
        render_in();
        USERNAME = in_username.value;
        PASSWORD = in_password.value;
        notes_get_all();
    }

};