const mobile_nav = document.querySelector(".mobile-navbar-btn");
const nav_header = document.querySelector(".header");

const toggleNavbar = () => {
  nav_header.classList.toggle("active");
};

mobile_nav.addEventListener("click", () => toggleNavbar());

const chat = document.querySelector(".chat");
const bot = document.querySelector(".bot");

function myFunc() {
  document.getElementsByClassName("chat").style.display = "none"
  document.getElementsById("botid").style.display = "block";
  console.log("hi");
}
bot.addEventListener("click", myFunc());
