(()=>{"use strict";function e(e){var t=e.value;if(e.nextElementSibling&&e.nextElementSibling.classList.contains("error_feedback")&&e.nextElementSibling.parentNode.removeChild(e.nextElementSibling),e.hasAttribute("required")&&(""==t||null==t)){var a=document.createElement("p");return a.classList.add("error_feedback"),a.innerText="This field is required",e.after(a),!1}if(e.getAttribute("max")&&parseInt(t)>parseInt(e.getAttribute("max"))){var n=document.createElement("p");return n.classList.add("error_feedback"),n.innerText="It cannot be greater than "+e.getAttribute("max"),e.after(n),!1}if(e.getAttribute("min")&&parseInt(t)<parseInt(e.getAttribute("min"))){var r=document.createElement("p");return r.classList.add("error_feedback"),r.innerText="It cannot be less than "+e.getAttribute("min"),e.after(r),!1}if(e.getAttribute("text-max")&&t.length>parseInt(e.getAttribute("max"))){var i=document.createElement("p");return i.classList.add("error_feedback"),i.innerText="It cannot be greater than "+e.getAttribute("max")+" characters",e.after(i),!1}if(e.getAttribute("text-min")&&t.length<parseInt(e.getAttribute("min"))){var c=document.createElement("p");return c.classList.add("error_feedback"),c.innerText="It cannot be less than "+e.getAttribute("min")+" characters",e.after(c),!1}if("email"==e.getAttribute("type")&&""!==e.value&&null!==e.value&&!t.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)){var o=document.createElement("p");return o.classList.add("error_feedback"),o.innerText="Please enter a valid email address.",e.after(o),!1}if(""!==e.value&&null!==e.value&&e.hasAttribute("type-link")){if(!function(e){if(/[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi.test(e))return!0;return!1}(t)){var l=document.createElement("p");return l.classList.add("error_feedback"),l.innerText="Please enter a valid link.",e.after(l),!1}t.startsWith("https://")||(e.value="https://"+t)}if(e.hasAttribute("max-files")){var s=e.getAttribute("max-files");if(e.files.length>s){var d=document.createElement("p");return d.classList.add("error_feedback"),d.innerText="You cannot upload more than ".concat(s," files."),e.after(d),!1}}return e.nextElementSibling&&e.nextElementSibling.classList.contains("error_feedback")&&e.nextElementSibling.parentNode.removeChild(e.nextElementSibling),!0}var t,a;function n(){var t=new FormData,a=document.querySelector("#svg-content"),n=document.querySelectorAll("[data-type='".concat($("[name='type']:checked").val(),"']")),r=["pdf","video"],i=0;if(function(e){return!!["expiry-management","pdf","social_link","images"].includes(e)}($("[name='type']:checked").val())||n.forEach((function(a){return e(a)?r.includes(a.name)&&a.value?t.append(a.name,a.files[0]):void t.append(a.name,a.value):i++})),i)return!1;t.append("type",$("[name='type']:checked").val()),t.append("_token",$("meta[name='csrf']").attr("content")),a.innerHTML="",$(".placeholder__image").hide(),$(".loader").removeClass("hidden"),$.ajax({url:"/my/get/qrcode/edit/preview/"+$("#qrcode").val(),type:"POST",data:t,processData:!1,contentType:!1,success:function(e){$(".loader").addClass("hidden");var t=JSON.parse(e);a.innerHTML=t.content},error:function(e){$(".loader").addClass("hidden"),$(".placeholder__image").show()}})}$("[name='type']").on("change",(function(){var e=$(this).val();$(".active_type").removeClass("active_type"),$("[for='".concat(e,"'] .qr-info__tab-content")).addClass("active_type"),$(".active_form").removeClass("active_form"),$(".qr-info__form-".concat(e)).addClass("active_form")})),$(".type").on("change",(function(){$(".error_feedback").remove()})),a=$("[name='type']:checked").val(),$(".active_type").removeClass("active_type"),$(".active_form").removeClass("active_form"),$("[for='".concat(a,"'] .qr-info__tab-content")).addClass("active_type"),$(".qr-info__form-".concat(a)).addClass("active_form"),$("[data-color-text]").on("change",(function(){var e=$(this).val();!e.startsWith("#")&&(e="#"+e),isHexColor(e)&&$("[name='".concat($(this).attr("data-color-text"),"']")).val(e)})),$("[data-color-input]").on("change",(function(){$("[data-color-text='".concat($(this).attr("name"),"']")).val($(this).val())})),document.querySelectorAll("[data-change]").forEach((function(e){e.addEventListener("input",(function(){clearTimeout(t),t=setTimeout((function(){n()}),1e3)}))})),$("#update-qrcode").on("click",(function(){var t,a,n=$(this),r=document.querySelectorAll("[data-type='".concat($("[name='type']:checked").val(),"']")),i=0,c=new FormData;if(r.forEach((function(t){return e(t)?"images"==t.name&&t.value?void t.files.forEach((function(e){c.append("images[]",e)})):function(e){return!!["pdf","social_logo"].includes(e)}(t.name)&&t.value?c.append(t.name,t.files[0]):void c.append(t.name,t.value):i++})),i)return!1;a="Updating",(t=n).attr("disabled",!0),t.text(a),c.append("type",$("[name='type']:checked").val()),c.append("_token",$("meta[name='csrf']").attr("content")),$.ajax({url:"/my/update/qrcode/"+$("#qrcode").val(),type:"POST",processData:!1,contentType:!1,data:c,success:function(){window.location.reload()},error:function(){!function(e,t){e.attr("disabled",!1),e.text(t)}(n,"Update"),Swal.fire({type:"error",title:"Oops...",text:"Something went wrong! There was an error updating the qrcode. Make sure you filled up the form with correct data.",confirmButtonClass:"btn btn-confirm mt-2"})},xhr:function(){var e=new window.XMLHttpRequest;return e.upload.addEventListener("progress",(function(e){if(e.lengthComputable){var t=e.loaded/e.total;$("#create-progress").css("width",100*t+"%")}}),!1),e}})})),n()})();