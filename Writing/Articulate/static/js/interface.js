
    // function myfunction() {
    //     document.getElementById("myDropdown").classList.toggle("show");
    // }

    // window.onclick = function(event) {
    //     if (!event.target.matches('.dropbtn')) {
    //         var myDropdown = document.getElementById("myDropdown");
    //           if (myDropdown.classList.contains('show')) {
    //             myDropdown.classList.remove('show');
    //           }
    //         }
    // }


// document.addEventListener('DOMContentLoaded', () => {

//     function showDropdown() {
//       const dropdown = document.querySelector('.dropdownMenu');
//       if (dropdown.style.display === 'none') {
//         dropdown.style.display = 'block';
//       } else {
//         dropdown.style.display = 'none';
//       }
//     }

//     document.querySelector('#username').onclick = showDropdown;
// });




document.addEventListener('DOMContentLoaded', () => {


    // When the user scrolls the page, execute myFunction
    window.onscroll = function() {myFunction()};

    // Get the navbar
    var navbar = document.querySelector(".header-home");

    // Get the offset position of the navbar
    var sticky = navbar.offsetTop;

    // Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
    function myFunction() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky")
    } else {
        navbar.classList.remove("sticky");
    }
    }



});


    // window.onscroll = function() {
    //     const navbar = document.querySelector('.header-home');
    //     var sticky = navbar.offsetTop;
    //     if (window.pageYOffset >= sticky) {
    //         //alert('Hello');
    //         navbar.style.top = 0;
    //         navbar.style.position = 'fixed';
    //     } else {
    //         navbar.style.top = sticky;
    //         navbar.style.position = 'relative';
    //     }
    // }