//Declaring and using packages
const exp = require("express");
const bp = require("body-parser");
const path = require("path");

//App to use express
const app = exp();
//Dinamic port
const port = process.env.PORT

//App use
app.use(exp.static(path.join(__dirname, "../public")));
//To use javascrip on html files
app.engine("html", require("ejs").renderFile)
app.set("view engine", "ejs")
//Setting views
app.set("views", path.join(__dirname, "views"))
//Routes
app.use("./routes/routes.js")

//Setting up server
app.listen(3000, () => {
  console.log("Server listening on port: ")
})
