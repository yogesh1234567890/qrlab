
(() => { 
    document.addEventListener("keypress", (function (t) { if ("Enter" == t.key)
     {
         var e = document.activeElement; 
         e.hasAttribute("data-qrcode-title-input") && e.blur() 
        
    } }));
    var nas=document.getElementById('nas').value

      var t = document.getElementsByClassName("edit-qrcode-title");
      t && t.forEach((function (t) { 
        t.addEventListener("click", (function () { 
        var t = this.parentNode, 
        e = t.getAttribute("data-qrcode-title-box"), 
        a = document.querySelector("input[data-qrcode-title-input='".concat(e, "']")); 
        t.classList.add("hidden"), a.classList.remove("hidden"), a.focus(), a.select() })) })); 
        var e = document.querySelectorAll("[data-qrcode-title-input]");
        e && e.forEach((function (t) { t.addEventListener("blur", (function () { 
        var t = this.getAttribute("data-qrcode-title-input"),
        e = document.querySelector("[data-qrcode-title-box='".concat(t, "']")); 
        document.querySelector("[data-qrcode-title-box='".concat(t, "'] .title-text")).innerText = this.value, 
        e.classList.remove("hidden"), this.classList.add("hidden"), this.blur() })), 
        e.forEach((function (t) { t.addEventListener("change", (function () { 
        var t = this.value; 
        var csrf = document.querySelector('meta[name="csrf-token"]').content;

        $.ajax({ 
            url: "qrtitleset/"+nas + this.getAttribute("data-qrcode-title-input"), 
            type: "POST", data: { title: t, _token:csrf  } })
        
        })) })) })) })();



            // t = data-qrcode-