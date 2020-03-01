var tl= new TimelineMax({onUpdate:updatePercentage});
const controller = new ScrollMagic.Controller();

tl.from('#welcome', .1, {x:-300, opacity: -5});

//tl.from('#video-fluid', .5 {x:500, opacity: 0});

const scene = new ScrollMagic.Scene({
    triggerElement: "with-video",
    triggerHook: "onEnter",
    duration: "80%"
})

    .setPin("col-lg-6")
    .setTween(tl)
        .addTo(controller);

function updatePercentage(){
    tl.progress();

}

/*
var tl2= new TimelineMax({onUpdate:updatePercentage2});
const controller2 = new ScrollMagic.Controller();

//tl.from('#welcome', .5, {x:-500, opacity: -5});

tl2.from('#gp-video', .5 {x:500, opacity: 0});

const scene2 = new ScrollMagic.Scene({
    triggerElement: "gp-video",
    triggerHook: "onEnter",
    duration: "80%"
})

    .setPin("col-lg-6")
    .setTween(tl2)
        .addTo(controller2);

function updatePercentage2(){
    tl2.progress();

}*/
