const { PythonShell } = require("python-shell");

let option = {
    scriptPath: "D:/New folder/sih-website",

};
PythonShell.run("pred.py", option, (err, res) => {
    if (err) console.log(err);
    if (res) console.log(res);
});

function shashank() {
    speed = document.getElementById('speed').value
    course = document.getElementById('course').value
    rot = document.getElementById('rot').value
    alert(speed + " " + course + " " + rot)
}