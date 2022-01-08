// Scripts to run when a page loads

//BASE HTML FUNCTIONS FOR OVERALL SITE
$(document).ready(function() {
            
    $('.popup-image').magnificPopup({
        type: 'image',
        mainClass: 'mfp-zoom',
        closeonContentClick: false,
        closeBtnInside: false,
        fixedContentPos: true,
        zoom: {
            enabled: false
        }
    });

    $('.gallery-popup-image').magnificPopup({
        type: 'image',
        mainClass: 'mfp-zoom',
        closeonContentClick: false,
        closeBtnInside: false,
        fixedContentPos: true,
        zoom: {
            enabled: true
        }
    });

    AOS.init();

    let body = document.querySelector('body')
    let footer =  document.querySelector('footer')
    // console.log(body.clientHeight)
    // console.log(body.scrollHeight)
    if (body.clientHeight >= body.scrollHeight) {
        footer.classList.add('fixed-bottom')
        // body.classList.add("d-flex justify-content-center align-items-center")
    }

});


//INDEX HTML FUNCTIONS

