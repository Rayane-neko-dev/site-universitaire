

/*=============== SHOW MENU ===============*/
const showMenu = (toggleId, navId) =>{
   const toggle = document.getElementById(toggleId),
         nav = document.getElementById(navId)

   toggle.addEventListener('click', () =>{
       // Add show-menu class to nav menu
       nav.classList.toggle('show-menu')

       // Add show-icon to show and hide the menu icon
       toggle.classList.toggle('show-icon')
   })
}

showMenu('nav-toggle','nav-menu')

$( document ).ready(function() {

     $('#slider1').owlCarousel({
        loop:true,
        margin:0,
        nav:true,
        autoplay: true,
                    animateOut: 'fadeOut', 
        dots: true,
        autoplayTimeout: 5000,
        navText:['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    })


     $('#slider3').owlCarousel({
        loop:true,
        margin:10,
        nav:true,
        autoplay: true,
        dots: true,
        autoplayTimeout: 5000,
        navText:['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:3
            }
        }
    })


      $('#slider2').owlCarousel({
        loop:true,
        margin:0,
        nav:true,
        autoplay: true,
        dots: true,
        autoplayTimeout: 5000,
        navText:['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:3
            }
        }
    })


});









$(document).ready(function(){

    $(".filter-button").click(function(){
        var value = $(this).attr('data-filter');
        
        if(value == "all")
        {
            //$('.filter').removeClass('hidden');
            $('.filter').show('1000');
        }
        else
        {
//            $('.filter[filter-item="'+value+'"]').removeClass('hidden');
//            $(".filter").not('.filter[filter-item="'+value+'"]').addClass('hidden');
            $(".filter").not('.'+value).hide('3000');
            $('.filter').filter('.'+value).show('3000');
            
        }
    });
    
    if ($(".filter-button").removeClass("active")) {
$(this).removeClass("active");
}
$(this).addClass("active");

});



//le compteur de stat



let valueDisplays = document.querySelectorAll(".num");
let interval = 3000;

valueDisplays.forEach((valueDisplay) => {
  let startValue = 0;
  let endValue = parseInt(valueDisplay.getAttribute("data-val"));
  let duration = Math.floor(interval / endValue);
  let counter = setInterval(function () {
    startValue += 1;
    if (startValue ==5000){startValue = endValue; }
    valueDisplay.textContent = startValue;
    if (startValue == endValue) {
      clearInterval(counter);
    }
  }, duration);
});

// script for changing language 


 //constant object translation for changing from the data attribute 
 
const translation = {
fr:{
home:"Home",
company:"Company",
analytics:"Analytics",
products:"Products",
users:"Users",

},
ar:{
home:"البحث العلمي",
company:"البحث",
analytics:"العلمي",
products:"العلمي",
users:"البحث",

},
};

//la logique 

const languageSelector = document.querySelector("select");

languageSelector.addEventListener("change",(event)=>{
setLanguage(event.target.value);
});

const setLanguage =(langue) =>{
const elements = document.querySelectorAll("[data-i18n]");
elements.forEach((element)=>{

const translationKey = element.getAttribute("data-i18n");
element.textContent = translation[langue][translationKey];

});
if(langue==='ar'){ document.dir = "rtl"}else{document.dir = "ltr"}
};


///////////////////////// buttons bourse et emploie ///////////////////////

const buttons = document.querySelectorAll(".conditions");

buttons.forEach(button => {
  button.addEventListener("click", () => {
    const section = button.closest(".popup");
    section.classList.add("active");
  });
});

document.querySelectorAll(".closebutton").forEach(button => {
  button.addEventListener("click", () => {
    const section4 = button.closest(".popup");
    section4.classList.remove("active");
  });
});



 
            // Popup functionality
            const buttonZ = document.querySelectorAll(".conditions2");
            buttonZ.forEach(buttoni => {
                buttoni.addEventListener("click", () => {
                    const section2 = buttoni.closest(".popup2");
                    section2.classList.add("active");
                });
            });

            document.querySelectorAll(".closebutton2").forEach(button => {
                button.addEventListener("click", () => {
                    const section3 = button.closest(".popup2");
                    section3.classList.remove("active");
                });
            });

            document.querySelectorAll(".overlay2").forEach(overlay => {
                overlay.addEventListener("click", () => {
                    const section3 = overlay.closest(".popup2");
                    section3.classList.remove("active");
                });
            });
    


  document.addEventListener('DOMContentLoaded', function() {
        const h2Elements = document.querySelectorAll('.second_h2');

        h2Elements.forEach(h2 => {
            h2.addEventListener('click', function() {
                const nextChangeText = this.nextElementSibling;
                
                if (nextChangeText && nextChangeText.classList.contains('change_text')) {
                    nextChangeText.classList.toggle('show');
                }
            });
        });
    });