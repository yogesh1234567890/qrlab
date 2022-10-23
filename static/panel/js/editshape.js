(() => {
    "use strict"; function e(e) { return !!["pdf", "social_logo"].includes(e) } function a(e) { var a = e.value; if (e.nextElementSibling && e.nextElementSibling.classList.contains("error_feedback") && e.nextElementSibling.parentNode.removeChild(e.nextElementSibling), e.hasAttribute("required") && ("" == a || null == a)) { var t = document.createElement("p"); return t.classList.add("error_feedback"), t.innerText = "This field is required", e.after(t), !1 } if (e.getAttribute("max") && parseInt(a) > parseInt(e.getAttribute("max"))) { var n = document.createElement("p"); return n.classList.add("error_feedback"), n.innerText = "It cannot be greater than " + e.getAttribute("max"), e.after(n), !1 } if (e.getAttribute("min") && parseInt(a) < parseInt(e.getAttribute("min"))) { var r = document.createElement("p"); return r.classList.add("error_feedback"), r.innerText = "It cannot be less than " + e.getAttribute("min"), e.after(r), !1 } if (e.getAttribute("text-max") && a.length > parseInt(e.getAttribute("max"))) { var o = document.createElement("p"); return o.classList.add("error_feedback"), o.innerText = "It cannot be greater than " + e.getAttribute("max") + " characters", e.after(o), !1 } if (e.getAttribute("text-min") && a.length < parseInt(e.getAttribute("min"))) { var c = document.createElement("p"); return c.classList.add("error_feedback"), c.innerText = "It cannot be less than " + e.getAttribute("min") + " characters", e.after(c), !1 } if ("email" == e.getAttribute("type") && "" !== e.value && null !== e.value && !a.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) { var l = document.createElement("p"); return l.classList.add("error_feedback"), l.innerText = "Please enter a valid email address.", e.after(l), !1 } if ("" !== e.value && null !== e.value && e.hasAttribute("type-link")) { if (!function (e) { if (/[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi.test(e)) return !0; return !1 }(a)) { var i = document.createElement("p"); return i.classList.add("error_feedback"), i.innerText = "Please enter a valid link.", e.after(i), !1 } a.startsWith("https://") || (e.value = "https://" + a) } if (e.hasAttribute("max-files")) { var s = e.getAttribute("max-files"); if (e.files.length > s) { var d = document.createElement("p"); return d.classList.add("error_feedback"), d.innerText = "You cannot upload more than ".concat(s, " files."), e.after(d), !1 } } return e.nextElementSibling && e.nextElementSibling.classList.contains("error_feedback") && e.nextElementSibling.parentNode.removeChild(e.nextElementSibling), !0 } var t; function n() {
        var nas = document.getElementById('nas').innerHTML 
        
    var t = document.querySelectorAll("[data-basic-input]"), n = new FormData, r = document.querySelector("#svg-content"), o = document.querySelectorAll("[data-type='".concat($("[name='type']:checked").val(), "']")), c = 0; if (o.forEach((function (t) { return a(t) ? "images" == t.name && t.value ? void t.files.forEach((function (e) { n.append("images[]", e) })) : e(t.name) && t.value ? n.append(t.name, t.files[0]) : void n.append(t.name, t.value) : c++ })), t.forEach((function (e) { if ("custom_logo" == e.name && e.value) return n.append(e.name, e.files[0]); n.append(e.name, e.value) })), c) return !1; $("[name='transparent_code']").is(":checked") && n.append("transparent_code", !0), $("[name='gradient']").is(":checked") && n.append("gradient", !0), $("[name='markers_color']").is(":checked") && n.append("markers_color", !0), $("[name='custom_logo']")[0].files.length > 0 && n.append("custom_logo", $("[name='custom_logo']")[0].files[0]), $("[name='radial']").is(":checked") && n.append("radial", !0), $("[name='no_logo_bg']").is(":checked") && n.append("no_logo_bg", !0), n.append("gradient_color", $("[name='gradient_color']").val()), n.append("pattern", $("[name='pattern']:checked").val()), n.append("marker_out", $("[name='marker_out']:checked").val()), n.append("marker_in", $("[name='marker_in']:checked").val()), n.append("optionlogo", $("[name='optionlogo']:checked").val()), n.append("outer_frame", $("[name='outer_frame']:checked").val()), n.append("framelabel", $("[name='framelabel']").val()), n.append("label_font", $("[name='label_font']").val()), n.append("type", $("[name='type']:checked").val()), n.append("_token", $("meta[name='csrf']").attr("content")), r.innerHTML = "", $(".placeholder__image").hide(), $(".loader").removeClass("hidden"),
        $.ajax({
                url: "/preditshapesave/"+nas,
                type: "POST", data: n,
                processData: !1,
                contentType: !1,
                success: function (e) {
                    $('#svg-content').html(e)
                    $(".loader").addClass("hidden");
                    var arr = e.split("}");
                    var str = arr[0] + "}";
                    // console.log(str);
                    var a = JSON.parse(str);
                    r.innerHTML = a.content
                },
                error: function (e) {
                    $(".loader").addClass("hidden"),
                    $(".placeholder__image").show()
                }
            })
    }
    function r() { var e = $("[name='type']:checked").val(), a = document.getElementById("static-checkbox"); return function (e) { return !!["expiry-management", "pdf", "social_link", "images"].includes(e) }(e) ? a.classList.add("hidden") : a.classList.remove("hidden") } $('[data-toggle="switchery"]').each((function () { new Switchery($(this)[0], $(this).data()) })), $("[name='type']").on("change", (function () { var e = $(this).val(); $(".active_type").removeClass("active_type"), $("[for='".concat(e, "'] .qr-info__tab-content")).addClass("active_type"), $(".active_form").removeClass("active_form"), $(".qr-info__form-".concat(e)).addClass("active_form"), r() })), $(".pattern_label").on("click", (function () { $(".pattern_label").removeClass("active_label"), $(this).addClass("active_label") })), $(".marker_label").on("click", (function () { $(".marker_label").removeClass("active_label"), $(this).addClass("active_label") })), $(".marker_center_label").on("click", (function () { $(".marker_center_label").removeClass("active_label"), $(this).addClass("active_label") })), $(".logo_label").on("click", (function () { $(".logo_label").removeClass("active_label"), $(this).addClass("active_label") })), $(".frame_label").on("click", (function () { $(".frame_label").removeClass("active_label"), $(this).addClass("active_label") })), $("[name='gradient']").on("change", (function () { $("#gradient_color_box").toggleClass("hidden") })), $(".browse_logo").on("click", (function () { $("[name='custom_logo']").click() })), $(".type").on("change", (function () { $(".error_feedback").remove() })), $("[name='custom_logo']").on("change", (function (e) { if ($("#custom_logo_filename").text($(this).val().split("\\").pop()), this.files[0].type.match("image.*")) { var a = this.files[0], t = new FileReader; t.onload = function (e) { $(".logo_label").removeClass("active_label"), $(".custom-watermark").removeClass("hidden"); var a = '<img src="' + e.target.result + '" class="user_watermark">'; $(".custom-watermark .hold-custom-watermark").html(a), $(".custom-watermark").addClass("active_label"), $("#custom_logo_input").attr("checked", !0) }, t.readAsDataURL(a) } setTimeout((function () { n() }), 100) })), $("[data-color-text]").on("change", (function () { var e = $(this).val(); !e.startsWith("#") && (e = "#" + e), /^#([a-f0-9]{6})$/i.test(e) && $("[name='".concat($(this).attr("data-color-text"), "']")).val(e) })), $("[data-color-input]").on("change", (function () { $("[data-color-text='".concat($(this).attr("name"), "']")).val($(this).val()) })), document.querySelectorAll("[data-change]").forEach((function (e) { e.addEventListener("input", (function () { clearTimeout(t), t = setTimeout((function () { n() }), 1e3) })) })), $("[name='pattern']").on("change", (function () { n() })), $("[name='marker_out']").on("change", (function () { n() })), $("[name='marker_in']").on("change", (function () { n() })), $("[name='optionlogo']").on("change", (function () { n() })), $("[name='outer_frame']").on("change", (function () { n() })),
        $("#create-qrcode").on("click",
            (function () {
                var nas = document.getElementById('nas').innerHTML 
                var t, n, r = $(this),
                o = document.querySelectorAll("[data-basic-input]"),
                c = document.querySelectorAll("[data-type='".concat($("[name='type']:checked").val(),
                    "']")), l = 0, i = new FormData;
                if (c.forEach((function (t) {
                    return a(t) ? "images" == t.name && t.value ?
                        void t.files.forEach((function (e) {
                            i.append("images[]", e)
                        })) : e(t.name) && t.value ? i.append(t.name, t.files[0]) : void
                            i.append(t.name, t.value) : l++
                })), l) return !1;
                n = "Submitting", (t = r).attr("disabled", !0),
                    t.text(n), o.forEach((function (e) {
                        if ("custom_logo" == e.name && e.value)
                            return i.append(e.name, e.files[0]); i.append(e.name, e.value)
                    })),
                    $("[name='status']").is(":checked") && i.append("status", !0),
                    $("[name='static']").is(":checked") && i.append("static", !0),
                    $("[name='transparent_code']").is(":checked") && i.append("transparent_code", !0),
                    $("[name='gradient']").is(":checked") && i.append("gradient", !0),
                    $("[name='markers_color']").is(":checked") && i.append("markers_color", !0),
                    $("[name='custom_logo']")[0].files.length > 0 && i.append("custom_logo",
                        $("[name='custom_logo']")[0].files[0]), $("[name='radial']")
                            .is(":checked") && i.append("radial", !0), $("[name='no_logo_bg']")
                                .is(":checked") && i.append("no_logo_bg", !0), i.append("gradient_color",
                                    $("[name='gradient_color']").val()), i.append("pattern",
                                        $("[name='pattern']:checked").val()), i.append("marker_out",
                                            $("[name='marker_out']:checked").val()), i.append("marker_in",
                                                $("[name='marker_in']:checked").val()), i.append("optionlogo",
                                                    $("[name='optionlogo']:checked").val()), i.append("outer_frame",
                                                        $("[name='outer_frame']:checked").val()), i.append("framelabel",
                                                            $("[name='framelabel']").val()), i.append("label_font",
                                                                $("[name='label_font']").val()), i.append("type",
                                                                    $("[name='type']:checked").val()),
                    i.append("_token",$("meta[name='csrf']").attr("content")),
                    $.ajax({
                        url: "/editshape/save/"+nas,
                        type: "POST", processData: !1,
                        contentType: !1, data: i,
                        success: function () { window.location.href = "/dashboard" },
                        error: function () {
                            !function (e, a) { e.attr("disabled", !1), e.text(a) }(r, "update"),
                            Swal.fire({
                                type: "error", title: "Oops...",
                                text: "Something went wrong! There was an error update the qrcode. Make sure you filled up the form with correct data.", confirmButtonClass: "btn btn-confirm mt-2"
                            })
                        }, xhr: function () { var e = new window.XMLHttpRequest; return e.upload.addEventListener("progress", (function (e) { if (e.lengthComputable) { var a = e.loaded / e.total; $("#create-progress").css("width", 100 * a + "%") } }), !1), e }
                    })
            })), r(); var o, c = new URL(window.location.href).searchParams; c.get("active") && (o = c.get("active"), $(".active_type").removeClass("active_type"), $(".active_form").removeClass("active_form"), $("[for='".concat(o, "'] .qr-info__tab-content")).addClass("active_type"), $(".qr-info__form-".concat(o)).addClass("active_form"))
})();