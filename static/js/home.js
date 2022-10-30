(() => {
    "use strict";
    var e = {
            146: (e, a, t) => {
                function n(e) {
                    return !!["pdf", "social_link", "images"].includes(e)
                }

                function r(e) {
                    return !!["pdf", "social_logo"].includes(e)
                }

                function o(e) {
                    var a = e.value;
                    if (e.nextElementSibling && e.nextElementSibling.classList.contains("error_feedback") && e.nextElementSibling.parentNode.removeChild(e.nextElementSibling), e.hasAttribute("required") && ("" == a || null == a)) {
                        var t = document.createElement("p");
                        return t.classList.add("error_feedback"), t.innerText = "This field is required", e.after(t), !1
                    }
                    if (e.getAttribute("max") && parseInt(a) > parseInt(e.getAttribute("max"))) {
                        var n = document.createElement("p");
                        return n.classList.add("error_feedback"), n.innerText = "It cannot be greater than " + e.getAttribute("max"), e.after(n), !1
                    }
                    if (e.getAttribute("min") && parseInt(a) < parseInt(e.getAttribute("min"))) {
                        var r = document.createElement("p");
                        return r.classList.add("error_feedback"), r.innerText = "It cannot be less than " + e.getAttribute("min"), e.after(r), !1
                    }
                    if (e.getAttribute("text-max") && a.length > parseInt(e.getAttribute("max"))) {
                        var o = document.createElement("p");
                        return o.classList.add("error_feedback"), o.innerText = "It cannot be greater than " + e.getAttribute("max") + " characters", e.after(o), !1
                    }
                    if (e.getAttribute("text-min") && a.length < parseInt(e.getAttribute("min"))) {
                        var c = document.createElement("p");
                        return c.classList.add("error_feedback"), c.innerText = "It cannot be less than " + e.getAttribute("min") + " characters", e.after(c), !1
                    }
                    if ("email" == e.getAttribute("type") && "" !== e.value && null !== e.value && !a.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
                        var l = document.createElement("p");
                        return l.classList.add("error_feedback"), l.innerText = "Please enter a valid email address.", e.after(l), !1
                    }
                    if ("" !== e.value && null !== e.value && e.hasAttribute("type-link")) {
                        if (! function(e) {
                                if (/[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi.test(e)) return !0;
                                return !1
                            }(a)) {
                            var i = document.createElement("p");
                            return i.classList.add("error_feedback"), i.innerText = "Please enter a valid link.", e.after(i), !1
                        }
                        a.startsWith("https://") || (e.value = "https://" + a)
                    }
                    if (e.hasAttribute("max-files")) {
                        var s = e.getAttribute("max-files");
                        if (e.files.length > s) {
                            var d = document.createElement("p");
                            return d.classList.add("error_feedback"), d.innerText = "You cannot upload more than ".concat(s, " files."), e.after(d), !1
                        }
                    }
                    return e.nextElementSibling && e.nextElementSibling.classList.contains("error_feedback") && e.nextElementSibling.parentNode.removeChild(e.nextElementSibling), !0
                }

                function c(e, a) {
                    var t = e.value.split("\\").pop();
                    document.getElementById(a).innerText = t
                }
                t.d(a, {
                    $6: () => n,
                    Dq: () => o,
                    RL: () => r,
                    f1: () => c
                })
            }
        },
        a = {};

    function t(n) {
        var r = a[n];
        if (void 0 !== r) return r.exports;
        var o = a[n] = {
            exports: {}
        };
        return e[n](o, o.exports, t), o.exports
    }
    t.d = (e, a) => {
        for (var n in a) t.o(a, n) && !t.o(e, n) && Object.defineProperty(e, n, {
            enumerable: !0,
            get: a[n]
        })
    }, t.o = (e, a) => Object.prototype.hasOwnProperty.call(e, a), (() => {
        var e, a = t(146);
        document.querySelectorAll("[data-change]").forEach((function(a) {
            a.addEventListener("input", (function() {
                clearTimeout(e), e = setTimeout((function() {
                    r()
                }), 1e3)
            }))
        })), $("[name='pattern']").on("change", (function() {
            r()
        })), $("[name='marker_out']").on("change", (function() {
            r()
        })), $("[name='marker_in']").on("change", (function() {
            r()
        })), $("[name='optionlogo']").on("change", (function() {
            r()
        })), $("[name='outer_frame']").on("change", (function() {
            r()
        })), $("[data-type-file]").on("change", (function() {
            var e = document.getElementById($(this).attr("id"));
            (0, a.f1)(e, $(this).attr("text-target"))
        }));
        var n = document.querySelectorAll("[data-social-btn]");

        function r() {
            var svgContent = document.getElementById("svg-content");
            var e = $("input[name='type']:checked").val(),

                t = document.querySelectorAll("[data-type='".concat(e, "']")),
                n = !1;
            if ($(".error_feedback").remove(), t.forEach((function(e) {
                    if (!(0, a.Dq)(e)) return n = !0
                })), n) return !1;
            ! function(e) {
                var t = document.querySelectorAll("[data-basic-input]"),
                    n = new FormData,
                    r = document.getElementById("svg-content");
                (0, a.$6)($("input[name='type']:checked").val()) || e.forEach((function(e) {
                    n.append(e.name, e.value)
                    // n.append("_token",$("meta[name='csrf']").attr("content"))

                }));
                t.forEach((function(e) {
                        if ("custom_logo" == e.name && e.value) return n.append(e.name, e.files[0]);
                        n.append(e.name, e.value)
                    })), $("[name='transparent_code']").is(":checked") && n.append("transparent_code", !0), $("[name='gradient']").is(":checked") && n.append("gradient", !0), $("[name='markers_color']").is(":checked") && n.append("markers_color", !0), $("[name='custom_logo']")[0].files.length > 0 && n.append("custom_logo", $("[name='custom_logo']")[0].files[0]), $("[name='gradient']").is(":checked") && n.append("gradient_color", $("[name='gradient_color']").val()), $("[name='radial']").is(":checked") && n.append("radial", !0), $("[name='no_logo_bg']").is(":checked") && n.append("no_logo_bg", !0), n.append("pattern", $("[name='pattern']:checked").val()), n.append("marker_out", $("[name='marker_out']:checked").val()), n.append("marker_in", $("[name='marker_in']:checked").val()), n.append("optionlogo", $("[name='optionlogo']:checked").val()), n.append("outer_frame", $("[name='outer_frame']:checked").val()), n.append("framelabel", $("[name='framelabel']").val()), n.append("label_font", $("[name='label_font']").val()), n.append("type", $("[name='type']:checked").val()), n.append("_token", $("meta[name='csrf']").attr("content")), r.innerHTML = "", $(".placeholder__image").hide(), $(".loader").removeClass("hidden"), c(),
                    $.ajax({
                url: "https://qrsample.qrlab.co/api/generate/qrcode",
                        type: "POST",
                        data: n,
                        processData: !1,
                        contentType: !1,
                        success: function(e) {
                            $(".loader").addClass("hidden");
                            var arr = e.split("}");
                            var result = JSON.parse(data);
                            console.log("manu")
                            console.log(result)
          svgContent.innerHTML = result.content;
                            var str = arr[0] + "}";
                            console.log(str);
                            var a = JSON.parse(str);
                            console.log(str);
                            r.innerHTML = a.content,
                                function() {
                                    var e = document.querySelector(".qr-generator__img svg"),
                                        a = (new XMLSerializer).serializeToString(e);
                                    a.match(/^<svg[^>]+xmlns="http\:\/\/www\.w3\.org\/2000\/svg"/) || (a = a.replace(/^<svg/, '<svg xmlns="http://www.w3.org/2000/svg"'));
                                    a.match(/^<svg[^>]+"http\:\/\/www\.w3\.org\/1999\/xlink"/) || (a = a.replace(/^<svg/, '<svg xmlns:xlink="http://www.w3.org/1999/xlink"'));
                                    a = '<?xml version="1.0" standalone="no"?>\r\n' + a;
                                    var t = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(a);
                                    $("#download-svg").attr("href", t), $("#download-svg").attr("download", !0), $("#download-svg").addClass("active_button"),
                                        function(e) {
                                            var a = "png",
                                                t = e,
                                                n = document.createElement("canvas"),
                                                r = n.getContext("2d"),
                                                o = new Image;
                                            o.onload = function() {
                                                var e = 2 * o.width,
                                                    t = 2 * o.height;
                                                n.width = e, n.height = t, r.clearRect(0, 0, e, t), r.drawImage(o, 0, 0, e, t);
                                                var c = n.toDataURL("image/" + a);
                                                $("#download-png").attr("href", c), $("#download-png").attr("download", !0), $("#download-png").addClass("active_button")
                                            }, o.src = t
                                        }(t)
                                }()
                        },
                        error: function(e) {
                            console.log("manu error")
                            $(".loader").addClass("hidden"), $(".placeholder__image").show(), c()
                        }
                    })
            }(t)
        }

        function o() {
            (0, a.$6)($("[name='type']:checked").val()) ? $("#save-qrcode").addClass("hidden"): $("#save-qrcode").removeClass("hidden")
        }

        function c() {
            $("#download-svg").attr("href", ""), $("#download-svg").attr("download", !1), $("#download-svg").removeClass("active_button"), $("#download-png").attr("href", ""), $("#download-png").attr("download", !1), $("#download-png").removeClass("active_button")
        }

        function l(e, a, t) {
            e.attr("disabled", !1), a.text(t)
        }
        n && n.forEach((function(e) {
            e.addEventListener("click", (function() {
                var a = e.getAttribute("data-social-btn");
                document.querySelector(".active-social-btn").classList.remove("active-social-btn"), this.classList.add("active-social-btn");
                var t = document.getElementById("social-inputs-box-".concat(a)),
                    n = document.querySelector(".active-social-inputs-box");
                n && n.classList.remove("active-social-inputs-box"), t.classList.add("active-social-inputs-box")
            }))
        })), $("[name='type']").on("change", (function() {
            var e = $(this).val();
            $(".active_type").removeClass("active_type"), $("[for='".concat(e, "'] .qr-info__tab-content")).addClass("active_type"), $(".active_form").removeClass("active_form"), $(".qr-info__form-".concat(e)).addClass("active_form")
        })), $("[name='custom_logo']").on("change", (function() {
            if ($("#custom_logo_filename").text($(this).val().split("\\").pop()), this.files[0].type.match("image.*")) {
                var e = this.files[0],
                    a = new FileReader;
                a.onload = function(e) {
                    $(".logo_label").removeClass("active_label"), $(".custom-watermark").removeClass("hidden");
                    var a = '<img src="' + e.target.result + '" class="user_watermark">';
                    $(".custom-watermark .hold-custom-watermark").html(a), $(".custom-watermark").addClass("active_label"), $("#custom_logo_input").attr("checked", !0)
                }, a.readAsDataURL(e)
            }
            setTimeout((function() {
                r()
            }), 100)
        })), $(".pattern_label").on("click", (function() {
            $(".pattern_label").removeClass("active_label"), $(this).addClass("active_label")
        })), $(".marker_label").on("click", (function() {
            $(".marker_label").removeClass("active_label"), $(this).addClass("active_label")
        })), $(".marker_center_label").on("click", (function() {
            $(".marker_center_label").removeClass("active_label"), $(this).addClass("active_label")
        })), $(".logo_label").on("click", (function() {
            $(".logo_label").removeClass("active_label"), $(this).addClass("active_label")
        })), $(".frame_label").on("click", (function() {
            $(".frame_label").removeClass("active_label"), $(this).addClass("active_label")
        })), $(".browse_logo").on("click", (function() {
            $("[name='custom_logo']").click()
        })), $("[name='gradient']").on("change", (function() {
            $("#gradient_color_box").toggleClass("hidden")
        })), $("[name='type']").on("change", (function() {
            $(".error_feedback").remove(), o()
        })), $("form").on("submit", (function(e) {
            e.preventDefault()
        })), $("#qr-download-btn-show").on("click", (function() {
            $(".qr-generator__btns").toggleClass("hidden")
        })), $("#images-input").on("change", (function() {
            var e = document.getElementById("qrcode-images");
            if (e.innerHTML = "", !(0, a.Dq)(document.getElementById("images-input"))) return !1;
            for (var t = this.files, n = "", r = 0; r < t.length; r++) {
                var o = t[r],
                    c = new FileReader;
                c.onload = function(a) {
                    n += '<img src="'.concat(a.target.result, '" alt="">'), e.innerHTML = n
                }, c.readAsDataURL(o)
            }
        })), $("[data-color-text]").on("change", (function() {
            var e = $(this).val();
            return !e.startsWith("#") && (e = "#" + e), /^#([a-f0-9]{6})$/i.test(e) && $("[name='".concat($(this).attr("data-color-text"), "']")).val(e), !1
        })), $("[data-color-input]").on("change", (function() {
            $("[data-color-text='".concat($(this).attr("name"), "']")).val($(this).val())
        })), $("#track-scans").on("click", (function() {
            var e = $(this),
                t = document.querySelectorAll("[data-basic-input]"),
                n = document.querySelectorAll("[data-type='".concat($("[name='type']:checked").val(), "']")),
                r = 0,
                o = new FormData;
            if (n.forEach((function(e) {
                    if (!(0, a.Dq)(e)) return r++;
                    if ("images" == e.name && e.value)
                        for (var t = 0; t < e.files.length; t++) o.append("images[]", e.files[t]);
                    else {
                        if ((0, a.RL)(e.name) && e.value) return o.append(e.name, e.files[0]);
                        o.append(e.name, e.value)
                    }
                })), r) return !1;
            var c = $("#track-scans-text");
            t.forEach((function(e) {
                if ("custom_logo" == e.name && e.value) return o.append(e.name, e.files[0]);
                o.append(e.name, e.value)
            })), $("[name='status']").is(":checked") && o.append("status", !0), $("[name='transparent_code']").is(":checked") && o.append("transparent_code", !0), $("[name='gradient']").is(":checked") && o.append("gradient", !0), $("[name='markers_color']").is(":checked") && o.append("markers_color", !0), $("[name='custom_logo']")[0].files.length > 0 && o.append("custom_logo", $("[name='custom_logo']")[0].files[0]), $("[name='radial']").is(":checked") && o.append("radial", !0), $("[name='no_logo_bg']").is(":checked") && o.append("no_logo_bg", !0), o.append("gradient_color", $("[name='gradient_color']").val()), o.append("pattern", $("[name='pattern']:checked").val()), o.append("marker_out", $("[name='marker_out']:checked").val()), o.append("marker_in", $("[name='marker_in']:checked").val()), o.append("optionlogo", $("[name='optionlogo']:checked").val()), o.append("outer_frame", $("[name='outer_frame']:checked").val()), o.append("framelabel", $("[name='framelabel']").val()), o.append("label_font", $("[name='label_font']").val()), o.append("type", $("[name='type']:checked").val()), o.append("_token", $("meta[name='csrf']").attr("content")), $.ajax({
                url: "/dashboard/create/save",
                type: "POST",
                processData: !1,
                contentType: !1,
                data: o,
                success: function() {
                    window.location.href = "/"
                },
                error: function(a) {
                    l(e, c, "Track number of scans"), 401 == a.status && (window.location.href = "/login")
                },
                xhr: function() {
                    var e = new window.XMLHttpRequest;
                    return e.upload.addEventListener("progress", (function(e) {
                        if (e.lengthComputable) {
                            var a = e.loaded / e.total;
                            $("#create-progress").css("width", 100 * a + "%")
                        }
                    }), !1), e
                }
            })
        })), $("#save-qrcode").on("click", (function() {
            var e = $(this),
                t = document.querySelectorAll("[data-basic-input]"),
                n = document.querySelectorAll("[data-type='".concat($("[name='type']:checked").val(), "']")),
                r = 0,
                o = new FormData;
            if (n.forEach((function(e) {
                    if (!(0, a.Dq)(e)) return r++;
                    if ("images" == e.name && e.value)
                        for (var t = 0; t < e.files.length; t++) o.append("images[]", e.files[t]);
                    else {
                        if ((0, a.RL)(e.name) && e.value) return o.append(e.name, e.files[0]);
                        o.append(e.name, e.value)
                    }
                })), r) return !1;
            var c = $("#track-scans-text");
            t.forEach((function(e) {
                if ("custom_logo" == e.name && e.value) return o.append(e.name, e.files[0]);
                o.append(e.name, e.value)
            })), $("[name='status']").is(":checked") && o.append("status", !0), $("[name='transparent_code']").is(":checked") && o.append("transparent_code", !0), $("[name='gradient']").is(":checked") && o.append("gradient", !0), $("[name='markers_color']").is(":checked") && o.append("markers_color", !0), $("[name='custom_logo']")[0].files.length > 0 && o.append("custom_logo", $("[name='custom_logo']")[0].files[0]), $("[name='radial']").is(":checked") && o.append("radial", !0), $("[name='no_logo_bg']").is(":checked") && o.append("no_logo_bg", !0), o.append("static", !0), o.append("gradient_color", $("[name='gradient_color']").val()), o.append("pattern", $("[name='pattern']:checked").val()), o.append("marker_out", $("[name='marker_out']:checked").val()), o.append("marker_in", $("[name='marker_in']:checked").val()), o.append("optionlogo", $("[name='optionlogo']:checked").val()), o.append("outer_frame", $("[name='outer_frame']:checked").val()), o.append("framelabel", $("[name='framelabel']").val()), o.append("label_font", $("[name='label_font']").val()), o.append("type", $("[name='type']:checked").val()), o.append("_token", $("meta[name='csrf']").attr("content")), 
            $.ajax({
                url: "/dashboard/create/save",
                type: "POST",
                processData: !1,
                contentType: !1,
                data: o,
                success: function() {
                    window.location.href = "/"
                },
                error: function(a) {
                    l(e, c, "Track number of scans"), 401 == a.status && (window.location.href = "/login")
                },
                xhr: function() {
                    var e = new window.XMLHttpRequest;
                    return e.upload.addEventListener("progress", (function(e) {
                        if (e.lengthComputable) {
                            var a = e.loaded / e.total;
                            $("#create-progress").css("width", 100 * a + "%")
                        }
                    }), !1), e
                }
            })
        })),
        
        

        o()
    })()
})();

