(() => {
    "use strict";
    var e = document.querySelectorAll("[data-social-btn]");
    e && e.forEach((function(e) {
        e.addEventListener("click", (function() {
            var t = e.getAttribute("data-social-btn");
            document.querySelector(".active-social-btn").classList.remove("active-social-btn"), this.classList.add("active-social-btn");
            var a = document.getElementById("social-inputs-box-".concat(t)),
                n = document.querySelector(".active-social-inputs-box");
            n && n.classList.remove("active-social-inputs-box"), a.classList.add("active-social-inputs-box")
        }))
    })), $("[data-type-file]").on("change", (function() {
        ! function(e, t) {
            var a = e.value.split("\\").pop();
            document.getElementById(t).innerText = a
        }(document.getElementById($(this).attr("id")), $(this).attr("text-target"))
    })), $("#images-input").on("change", (function() {
        var e = document.getElementById("qrcode-images");
        if (e.innerHTML = "", ! function(e) {
                var t = e.value;
                if (e.nextElementSibling && e.nextElementSibling.classList.contains("error_feedback") && e.nextElementSibling.parentNode.removeChild(e.nextElementSibling), e.hasAttribute("required") && ("" == t || null == t)) {
                    var a = document.createElement("p");
                    return a.classList.add("error_feedback"), a.innerText = "This field is required", e.after(a), !1
                }
                if (e.getAttribute("max") && parseInt(t) > parseInt(e.getAttribute("max"))) {
                    var n = document.createElement("p");
                    return n.classList.add("error_feedback"), n.innerText = "It cannot be greater than " + e.getAttribute("max"), e.after(n), !1
                }
                if (e.getAttribute("min") && parseInt(t) < parseInt(e.getAttribute("min"))) {
                    var r = document.createElement("p");
                    return r.classList.add("error_feedback"), r.innerText = "It cannot be less than " + e.getAttribute("min"), e.after(r), !1
                }
                if (e.getAttribute("text-max") && t.length > parseInt(e.getAttribute("max"))) {
                    var i = document.createElement("p");
                    return i.classList.add("error_feedback"), i.innerText = "It cannot be greater than " + e.getAttribute("max") + " characters", e.after(i), !1
                }
                if (e.getAttribute("text-min") && t.length < parseInt(e.getAttribute("min"))) {
                    var s = document.createElement("p");
                    return s.classList.add("error_feedback"), s.innerText = "It cannot be less than " + e.getAttribute("min") + " characters", e.after(s), !1
                }
                if ("email" == e.getAttribute("type") && "" !== e.value && null !== e.value && !t.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
                    var c = document.createElement("p");
                    return c.classList.add("error_feedback"), c.innerText = "Please enter a valid email address.", e.after(c), !1
                }
                if ("" !== e.value && null !== e.value && e.hasAttribute("type-link")) {
                    if (!/[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi.test(t)) {
                        var l = document.createElement("p");
                        return l.classList.add("error_feedback"), l.innerText = "Please enter a valid link.", e.after(l), !1
                    }
                    t.startsWith("https://") || (e.value = "https://" + t)
                }
                if (e.hasAttribute("max-files")) {
                    var o = e.getAttribute("max-files");
                    if (e.files.length > o) {
                        var u = document.createElement("p");
                        return u.classList.add("error_feedback"), u.innerText = "You cannot upload more than ".concat(o, " files."), e.after(u), !1
                    }
                }
                return e.nextElementSibling && e.nextElementSibling.classList.contains("error_feedback") && e.nextElementSibling.parentNode.removeChild(e.nextElementSibling), !0
            }(document.getElementById("images-input"))) return !1;
        var t = this.files,
            a = "";
        t.forEach((function(t) {
            var n = new FileReader;
            n.onload = function(t) {
                a += '<img src="'.concat(t.target.result, '" alt="">'), e.innerHTML = a
            }, n.readAsDataURL(t)
        }))
    }))
})();