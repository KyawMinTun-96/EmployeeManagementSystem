function click_drawer() {
    var nav    = document.querySelector(".page_group .navigation");
    var p_body = document.querySelector(".page_group .page_body")
    if(nav.style.left == 0 | nav.style.left == "0px") {

        nav.style.transition = "ease .5s";
        nav.style.left = "-190px";
        p_body.style.transition = "ease .5s";
        p_body.style.marginLeft = "0px";

    }else {

        nav.style.transition = "ease .5s";
        nav.style.left = "0";
        p_body.style.transition = "ease .5s";
        p_body.style.marginLeft = "190px";

    }
}



