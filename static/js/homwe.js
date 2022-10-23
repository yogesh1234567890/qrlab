/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./static/main/js/utilities.js":
/*!****************************************!*\
  !*** ./resources/main/js/utilities.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

    __webpack_require__.r(__webpack_exports__);
    /* harmony export */ __webpack_require__.d(__webpack_exports__, {
    /* harmony export */   "activeType": () => (/* binding */ activeType),
    /* harmony export */   "checkAndRenderError": () => (/* binding */ checkAndRenderError),
    /* harmony export */   "isFileType": () => (/* binding */ isFileType),
    /* harmony export */   "isHexColor": () => (/* binding */ isHexColor),
    /* harmony export */   "isLink": () => (/* binding */ isLink),
    /* harmony export */   "isPureDynamic": () => (/* binding */ isPureDynamic),
    /* harmony export */   "load": () => (/* binding */ load),
    /* harmony export */   "setTextOnImageUpload": () => (/* binding */ setTextOnImageUpload),
    /* harmony export */   "stopLoad": () => (/* binding */ stopLoad),
    /* harmony export */   "validateEmail": () => (/* binding */ validateEmail)
    /* harmony export */ });
    function validateEmail(email) {
      return email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/);
    }
    
    function isPureDynamic(type) {
      var dynamic_qrcodes = ["expiry-management", "pdf", "social_link", "images"];
    
      if (dynamic_qrcodes.includes(type)) {
        return true;
      }
    
      return false;
    }
    
    function isFileType(type) {
      var file_names = ["pdf", "social_logo"];
    
      if (file_names.includes(type)) {
        return true;
      }
    
      return false;
    }
    
    function isLink(link) {
      var regex = /[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi;
    
      if (regex.test(link)) {
        return true;
      }
    
      return false;
    }
    
    function activeType(type) {
      $(".active_type").removeClass("active_type");
      $(".active_form").removeClass("active_form");
      $("[for='".concat(type, "'] .qr-info__tab-content")).addClass("active_type");
      $(".qr-info__form-".concat(type)).addClass("active_form");
    }
    
    function isHexColor(color) {
      var regex = /^#([a-f0-9]{6})$/i;
      return regex.test(color);
    }
    
    function load(elem, text) {
      elem.attr("disabled", true);
      elem.text(text);
    }
    
    function stopLoad(elem, text) {
      elem.attr("disabled", false);
      elem.text(text);
    }
    
    function checkAndRenderError(input) {
      var value = input.value;
    
      if (input.nextElementSibling) {
        if (input.nextElementSibling.classList.contains("error_feedback")) {
          input.nextElementSibling.parentNode.removeChild(input.nextElementSibling);
        }
      }
    
      if (input.hasAttribute("required")) {
        if (value == "" || value == null) {
          var p = document.createElement("p");
          p.classList.add("error_feedback");
          p.innerText = "This field is required";
          input.after(p);
          return false;
        }
      }
    
      if (input.getAttribute("max")) {
        if (parseInt(value) > parseInt(input.getAttribute("max"))) {
          var _p = document.createElement("p");
    
          _p.classList.add("error_feedback");
    
          _p.innerText = "It cannot be greater than " + input.getAttribute("max");
          input.after(_p);
          return false;
        }
      }
    
      if (input.getAttribute("min")) {
        if (parseInt(value) < parseInt(input.getAttribute("min"))) {
          var _p2 = document.createElement("p");
    
          _p2.classList.add("error_feedback");
    
          _p2.innerText = "It cannot be less than " + input.getAttribute("min");
          input.after(_p2);
          return false;
        }
      }
    
      if (input.getAttribute("text-max")) {
        if (value.length > parseInt(input.getAttribute("max"))) {
          var _p3 = document.createElement("p");
    
          _p3.classList.add("error_feedback");
    
          _p3.innerText = "It cannot be greater than " + input.getAttribute("max") + " characters";
          input.after(_p3);
          return false;
        }
      }
    
      if (input.getAttribute("text-min")) {
        if (value.length < parseInt(input.getAttribute("min"))) {
          var _p4 = document.createElement("p");
    
          _p4.classList.add("error_feedback");
    
          _p4.innerText = "It cannot be less than " + input.getAttribute("min") + " characters";
          input.after(_p4);
          return false;
        }
      }
    
      if (input.getAttribute("type") == "email" && input.value !== "" && input.value !== null) {
        if (!validateEmail(value)) {
          var _p5 = document.createElement("p");
    
          _p5.classList.add("error_feedback");
    
          _p5.innerText = "Please enter a valid email address.";
          input.after(_p5);
          return false;
        }
      }
    
      if (input.value !== "" && input.value !== null) {
        if (input.hasAttribute("type-link")) {
          if (!isLink(value)) {
            var _p6 = document.createElement("p");
    
            _p6.classList.add("error_feedback");
    
            _p6.innerText = "Please enter a valid link.";
            input.after(_p6);
            return false;
          }
    
          if (!value.toLowerCase().startsWith("https://")) {
            if (value.toLowerCase() !== "http://") {
              input.value = "https://" + value;
            }
          }
        }
      }
    
      if (input.hasAttribute("max-files")) {
        var maxFiles = input.getAttribute("max-files");
    
        if (input.files.length > maxFiles) {
          var _p7 = document.createElement("p");
    
          _p7.classList.add("error_feedback");
    
          _p7.innerText = "You cannot upload more than ".concat(maxFiles, " files.");
          input.after(_p7);
          return false;
        }
      }
    
      function isLink(link) {
        var regex = /[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/gi;
    
        if (regex.test(link)) {
          return true;
        }
    
        return false;
      }
    
      if (input.nextElementSibling) {
        if (input.nextElementSibling.classList.contains("error_feedback")) {
          input.nextElementSibling.parentNode.removeChild(input.nextElementSibling);
        }
      }
    
      return true;
    }
    
    function setTextOnImageUpload(input, textElementId) {
      var text = input.value.split("\\").pop();
      var textElement = document.getElementById(textElementId);
      textElement.innerText = text;
    }
    
    
    
    /***/ })
    
    /******/ 	});
    /************************************************************************/
    /******/ 	// The module cache
    /******/ 	var __webpack_module_cache__ = {};
    /******/ 	
    /******/ 	// The require function
    /******/ 	function __webpack_require__(moduleId) {
    /******/ 		// Check if module is in cache
    /******/ 		var cachedModule = __webpack_module_cache__[moduleId];
    /******/ 		if (cachedModule !== undefined) {
    /******/ 			return cachedModule.exports;
    /******/ 		}
    /******/ 		// Create a new module (and put it into the cache)
    /******/ 		var module = __webpack_module_cache__[moduleId] = {
    /******/ 			// no module.id needed
    /******/ 			// no module.loaded needed
    /******/ 			exports: {}
    /******/ 		};
    /******/ 	
    /******/ 		// Execute the module function
    /******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
    /******/ 	
    /******/ 		// Return the exports of the module
    /******/ 		return module.exports;
    /******/ 	}
    /******/ 	
    /************************************************************************/
    /******/ 	/* webpack/runtime/define property getters */
    /******/ 	(() => {
    /******/ 		// define getter functions for harmony exports
    /******/ 		__webpack_require__.d = (exports, definition) => {
    /******/ 			for(var key in definition) {
    /******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
    /******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
    /******/ 				}
    /******/ 			}
    /******/ 		};
    /******/ 	})();
    /******/ 	
    /******/ 	/* webpack/runtime/hasOwnProperty shorthand */
    /******/ 	(() => {
    /******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
    /******/ 	})();
    /******/ 	
    /******/ 	/* webpack/runtime/make namespace object */
    /******/ 	(() => {
    /******/ 		// define __esModule on exports
    /******/ 		__webpack_require__.r = (exports) => {
    /******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
    /******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
    /******/ 			}
    /******/ 			Object.defineProperty(exports, '__esModule', { value: true });
    /******/ 		};
    /******/ 	})();
    /******/ 	
    /************************************************************************/
    var __webpack_exports__ = {};
    // This entry need to be wrapped in an IIFE because it need to be isolated against other modules in the chunk.
    (() => {
    /*!***********************************!*\
      !*** ./resources/main/js/home.js ***!
      \***********************************/
    __webpack_require__.r(__webpack_exports__);
    /* harmony import */ var _utilities__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./utilities */ "./resources/main/js/utilities.js");
    
    var timer; // -------------------- Constants & Elements Start Here --------------------
    
    var NO_PREVIEW_TYPES = new Set(["pdf", "svg", "png"]);
    var DOWNLOAD_BTN_WRAP_CLASS = ".qr-download-btn-wrap";
    var GENERATE_QR_CODE_BTN_ID = "#generate-qr-code"; // -------------------- Constants & Elements End Here --------------------
    // Generating Qrcode
    
    var inputs = document.querySelectorAll("[data-change]");
    inputs.forEach(function (input) {
      input.addEventListener("input", function () {
        clearTimeout(timer);
        timer = setTimeout(function () {
          validateByTypeAndDisplay();
        }, 1000);
      });
    });
    $("[name='pattern']").on("change", function () {
      validateByTypeAndDisplay();
    });
    $("[name='marker_out']").on("change", function () {
      validateByTypeAndDisplay();
    });
    $("[name='marker_in']").on("change", function () {
      validateByTypeAndDisplay();
    });
    $("[name='optionlogo']").on("change", function () {
      validateByTypeAndDisplay();
    });
    $("[name='outer_frame']").on("change", function () {
      validateByTypeAndDisplay();
    });
    $("[data-type-file]").on("change", function () {
      if (this.files[0]) {
        $(GENERATE_QR_CODE_BTN_ID).show();
      } else {
        $(GENERATE_QR_CODE_BTN_ID).hide();
      }
    
      var input = document.getElementById($(this).attr("id"));
      (0,_utilities__WEBPACK_IMPORTED_MODULE_0__.setTextOnImageUpload)(input, $(this).attr("text-target"));
    });
    var socialBtns = document.querySelectorAll("[data-social-btn]");
    
    if (socialBtns) {
      socialBtns.forEach(function (socialBtn) {
        socialBtn.addEventListener("click", function () {
          var type = socialBtn.getAttribute("data-social-btn"); // button
    
          var activeBtn = document.querySelector(".active-social-btn");
          activeBtn.classList.remove("active-social-btn");
          this.classList.add("active-social-btn"); // inputs box
    
          var socialInputsBox = document.getElementById("social-inputs-box-".concat(type));
          var previousSocialInputsBox = document.querySelector(".active-social-inputs-box");
          previousSocialInputsBox ? previousSocialInputsBox.classList.remove("active-social-inputs-box") : "";
          socialInputsBox.classList.add("active-social-inputs-box");
        });
      });
    }
    
    $("[name='type']").on("change", function () {
      var value = $(this).val();
      $(".active_type").removeClass("active_type");
      $("[for='".concat(value, "'] .qr-info__tab-content")).addClass("active_type");
      $(".active_form").removeClass("active_form");
      $(".qr-info__form-".concat(value)).addClass("active_form");
    
      if (NO_PREVIEW_TYPES.has(value)) {
        hideDownloadAndSaveButtons();
      } else {
        showDownloadAndSaveButtons();
      }
    
      $(GENERATE_QR_CODE_BTN_ID).hide();
    });
    $("[name='custom_logo']").on("change", function () {
      $("#custom_logo_filename").text($(this).val().split("\\").pop());
    
      if (this.files[0].type.match("image.*")) {
        var file = this.files[0];
        var reader = new FileReader();
    
        reader.onload = function (e) {
          $(".logo_label").removeClass("active_label");
          $(".custom-watermark").removeClass("hidden");
          var out = '<img src="' + e.target.result + '" class="user_watermark">';
          $(".custom-watermark .hold-custom-watermark").html(out);
          $(".custom-watermark").addClass("active_label");
          $("#custom_logo_input").attr("checked", true);
        };
    
        reader.readAsDataURL(file);
      }
    
      setTimeout(function () {
        validateByTypeAndDisplay();
      }, 100);
    });
    
    function hideDownloadAndSaveButtons() {
      $(DOWNLOAD_BTN_WRAP_CLASS).hide();
    }
    
    function showDownloadAndSaveButtons() {
      $(DOWNLOAD_BTN_WRAP_CLASS).show();
    }
    
    function validateByTypeAndDisplay() {
      var type = $("input[name='type']:checked").val();
      var typeInputs = document.querySelectorAll("[data-type='".concat(type, "']"));
      var hasError = false;
      $(".error_feedback").remove();
      typeInputs.forEach(function (input) {
        if (!(0,_utilities__WEBPACK_IMPORTED_MODULE_0__.checkAndRenderError)(input)) {
          return hasError = true;
        }
      });
      if (hasError) return false;
    
      if (NO_PREVIEW_TYPES.has(type)) {
        return;
      }
    
      showDownloadAndSaveButtons();
      displayPreview(typeInputs);
    }
    
    function displayPreview(inputs) {
      var olfInputs = document.querySelectorAll("[data-basic-input]");
      var formData = new FormData();
      var svgContent = document.getElementById("svg-content");
    
      if (!(0,_utilities__WEBPACK_IMPORTED_MODULE_0__.isPureDynamic)($("input[name='type']:checked").val())) {
        inputs.forEach(function (input) {
          formData.append(input.name, input.value);
        });
      }
    
      olfInputs.forEach(function (input) {
        if (input.name == "custom_logo" && input.value) {
          return formData.append(input.name, input.files[0]);
        }
    
        formData.append(input.name, input.value);
      }); // Checkbox
    
      $("[name='transparent_code']").is(":checked") ? formData.append("transparent_code", true) : "";
      $("[name='gradient']").is(":checked") ? formData.append("gradient", true) : "";
      $("[name='markers_color']").is(":checked") ? formData.append("markers_color", true) : "";
      $("[name='custom_logo']")[0].files.length > 0 ? formData.append("custom_logo", $("[name='custom_logo']")[0].files[0]) : "";
      $("[name='gradient']").is(":checked") ? formData.append("gradient_color", $("[name='gradient_color']").val()) : "";
      $("[name='radial']").is(":checked") ? formData.append("radial", true) : "";
      $("[name='no_logo_bg']").is(":checked") ? formData.append("no_logo_bg", true) : ""; // Radios
    
      formData.append("pattern", $("[name='pattern']:checked").val());
      formData.append("marker_out", $("[name='marker_out']:checked").val());
      formData.append("marker_in", $("[name='marker_in']:checked").val());
      formData.append("optionlogo", $("[name='optionlogo']:checked").val());
      formData.append("outer_frame", $("[name='outer_frame']:checked").val()); // Frame
    
      formData.append("framelabel", $("[name='framelabel']").val());
      formData.append("label_font", $("[name='label_font']").val());
      formData.append("type", $("[name='type']:checked").val());
      formData.append("_token", $("meta[name='csrf']").attr("content"));
      svgContent.innerHTML = "";
      $(".placeholder__image").hide();
      $(".loader").removeClass("hidden");
      disableDownloads();
      $.ajax({
        url: "/dashboard/create/save",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function success(data) {
          $(".loader").addClass("hidden");           
          var result = JSON.parse(data);
          svgContent.innerHTML = result.content;
          setDownloads();
        },
        error: function error(_error) {
          $(".loader").addClass("hidden");
          $(".placeholder__image").show();
          disableDownloads();
        }
      });
    }
    
    $(".pattern_label").on("click", function () {
      $(".pattern_label").removeClass("active_label");
      $(this).addClass("active_label");
    });
    $(".marker_label").on("click", function () {
      $(".marker_label").removeClass("active_label");
      $(this).addClass("active_label");
    });
    $(".marker_center_label").on("click", function () {
      $(".marker_center_label").removeClass("active_label");
      $(this).addClass("active_label");
    });
    $(".logo_label").on("click", function () {
      $(".logo_label").removeClass("active_label");
      $(this).addClass("active_label");
    });
    $(".frame_label").on("click", function () {
      $(".frame_label").removeClass("active_label");
      $(this).addClass("active_label");
    });
    $(".browse_logo").on("click", function () {
      $("[name='custom_logo']").click();
    });
    $("[name='gradient']").on("change", function () {
      $("#gradient_color_box").toggleClass("hidden");
    });
    $("[name='type']").on("change", function () {
      $(".error_feedback").remove();
      processSaveQrCode();
    });
    $("form").on("submit", function (e) {
      e.preventDefault();
    });
    $("#qr-download-btn-show").on("click", function () {
      $(".qr-generator__btns").toggleClass("hidden");
    });
    $("#images-input").on("change", function () {
      var imagesContainer = document.getElementById("qrcode-images");
      imagesContainer.innerHTML = "";
    
      if (!(0,_utilities__WEBPACK_IMPORTED_MODULE_0__.checkAndRenderError)(document.getElementById("images-input"))) {
        return false;
      }
    
      var files = this.files;
      var images = "";
    
      for (var i = 0; i < files.length; i++) {
        var file = files[i];
        var reader = new FileReader();
    
        reader.onload = function (e) {
          images += "<img src=\"".concat(e.target.result, "\" alt=\"\">");
          imagesContainer.innerHTML = images;
        };
    
        reader.readAsDataURL(file);
      }
    }); // ------------ Color text & Color inputs --------------------
    
    $("[data-color-text]").on("change", function () {
      var val = $(this).val();
      !val.startsWith("#") ? val = "#" + val : "";
    
      if (isHexColor(val)) {
        $("[name='".concat($(this).attr("data-color-text"), "']")).val(val);
      }
    
      return false;
    });
    $("[data-color-input]").on("change", function () {
      var target = $("[data-color-text='".concat($(this).attr("name"), "']"));
      target.val($(this).val());
    }); // -------------------- Functions --------------------
    
    function processSaveQrCode() {
      return; // if (isPureDynamic($("[name='type']:checked").val())) {
      //     $("#save-qrcode").addClass("hidden");
      // } else {
      //     $("#save-qrcode").removeClass("hidden");
      // }
    } // Check if input has error
    
    
    function setDownloads() {
      //  SET SVG
      var svg = document.querySelector(".qr-generator__img svg");
      var serializer = new XMLSerializer();
      var source = serializer.serializeToString(svg);
    
      if (!source.match(/^<svg[^>]+xmlns="http\:\/\/www\.w3\.org\/2000\/svg"/)) {
        source = source.replace(/^<svg/, '<svg xmlns="http://www.w3.org/2000/svg"');
      }
    
      if (!source.match(/^<svg[^>]+"http\:\/\/www\.w3\.org\/1999\/xlink"/)) {
        source = source.replace(/^<svg/, '<svg xmlns:xlink="http://www.w3.org/1999/xlink"');
      }
    
      source = '<?xml version="1.0" standalone="no"?>\r\n' + source;
      var url = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(source);
      $("#download-svg").attr("href", url);
      $("#download-svg").attr("download", true);
      $("#download-svg").addClass("active_button"); // SET PNG
    
      setPngDownload(url);
    }
    
    function setPngDownload(svg) {
      var format = "png";
      var svgData = svg;
      var canvas = document.createElement("canvas");
      var context = canvas.getContext("2d");
      var image = new Image();
    
      image.onload = function () {
        var newImgW = image.width * 2;
        var newImgH = image.height * 2;
        canvas.width = newImgW;
        canvas.height = newImgH;
        context.clearRect(0, 0, newImgW, newImgH);
        context.drawImage(image, 0, 0, newImgW, newImgH);
        var pngData = canvas.toDataURL("image/" + format);
        $("#download-png").attr("href", pngData);
        $("#download-png").attr("download", true);
        $("#download-png").addClass("active_button");
      };
    
      image.src = svgData;
    }
    
    function disableDownloads() {
      // SVG
      $("#download-svg").attr("href", "");
      $("#download-svg").attr("download", false);
      $("#download-svg").removeClass("active_button"); // PNG
    
      $("#download-png").attr("href", "");
      $("#download-png").attr("download", false);
      $("#download-png").removeClass("active_button");
    }
    
    function isHexColor(color) {
      var regex = /^#([a-f0-9]{6})$/i;
      return regex.test(color);
    }
    
    function load(elem, textElem, text) {
      elem.attr("disabled", true);
      textElem.text(text);
    }
    
    function stopLoad(elem, textElem, text) {
      elem.attr("disabled", false);
      textElem.text(text);
    } // -------------------- Create QrCode --------------------
    
    
    function trackScans(thisEl) {
      var olfInputs = document.querySelectorAll("[data-basic-input]");
      var stepInputs = document.querySelectorAll("[data-type='".concat($("[name='type']:checked").val(), "']"));
      var hasError = 0;
      var formData = new FormData();
      stepInputs.forEach(function (input) {
        if (!(0,_utilities__WEBPACK_IMPORTED_MODULE_0__.checkAndRenderError)(input)) {
          return hasError++;
        }
    
        if (input.name == "images" && input.value) {
          for (var i = 0; i < input.files.length; i++) {
            formData.append("images[]", input.files[i]);
          }
    
          return;
        }
    
        if ((0,_utilities__WEBPACK_IMPORTED_MODULE_0__.isFileType)(input.name) && input.value) {
          return formData.append(input.name, input.files[0]);
        }
    
        formData.append(input.name, input.value);
      });
    
      if (hasError) {
        return false;
      }
    
      var textElem = $("#track-scans-text"); // load(thisEl, textElem, "Preparing for track");
    
      olfInputs.forEach(function (input) {
        if (input.name == "custom_logo" && input.value) {
          return formData.append(input.name, input.files[0]);
        }
    
        formData.append(input.name, input.value);
      }); // Checkboxes
    
      $("[name='status']").is(":checked") ? formData.append("status", true) : "";
      $("[name='transparent_code']").is(":checked") ? formData.append("transparent_code", true) : "";
      $("[name='gradient']").is(":checked") ? formData.append("gradient", true) : "";
      $("[name='markers_color']").is(":checked") ? formData.append("markers_color", true) : "";
      $("[name='custom_logo']")[0].files.length > 0 ? formData.append("custom_logo", $("[name='custom_logo']")[0].files[0]) : "";
      $("[name='radial']").is(":checked") ? formData.append("radial", true) : "";
      $("[name='no_logo_bg']").is(":checked") ? formData.append("no_logo_bg", true) : "";
      formData.append("gradient_color", $("[name='gradient_color']").val()); // Radios
    
      formData.append("pattern", $("[name='pattern']:checked").val());
      formData.append("marker_out", $("[name='marker_out']:checked").val());
      formData.append("marker_in", $("[name='marker_in']:checked").val());
      formData.append("optionlogo", $("[name='optionlogo']:checked").val());
      formData.append("outer_frame", $("[name='outer_frame']:checked").val()); // Frame
    
      formData.append("framelabel", $("[name='framelabel']").val());
      formData.append("label_font", $("[name='label_font']").val());
      formData.append("type", $("[name='type']:checked").val());
      formData.append("_token", $("meta[name='csrf']").attr("content"));
      $.ajax({
        url: "/qrcode/track/scans",
        type: "POST",
        processData: false,
        contentType: false,
        data: formData,
        success: function success() {
          window.location.href = "/my/qrcodes";
        },
        error: function error(_error2) {
          stopLoad(thisEl, textElem, "Track number of scans");
    
          if (_error2.status == 401) {
            window.location.href = "/login";
          }
        },
        xhr: function xhr() {
          var xhr = new window.XMLHttpRequest();
          xhr.upload.addEventListener("progress", function (evt) {
            if (evt.lengthComputable) {
              var percentComplete = evt.loaded / evt.total;
              $("#create-progress").css("width", percentComplete * 100 + "%");
            }
          }, false);
          return xhr;
        }
      });
    }
    
    function saveQrCode(thiEl) {
      var olfInputs = document.querySelectorAll("[data-basic-input]");
      var stepInputs = document.querySelectorAll("[data-type='".concat($("[name='type']:checked").val(), "']"));
      var hasError = 0;
      var formData = new FormData();
      stepInputs.forEach(function (input) {
        if (!(0,_utilities__WEBPACK_IMPORTED_MODULE_0__.checkAndRenderError)(input)) {
          return hasError++;
        }
    
        if (input.name == "images" && input.value) {
          for (var i = 0; i < input.files.length; i++) {
            formData.append("images[]", input.files[i]);
          }
    
          return;
        }
    
        if ((0,_utilities__WEBPACK_IMPORTED_MODULE_0__.isFileType)(input.name) && input.value) {
          return formData.append(input.name, input.files[0]);
        }
    
        formData.append(input.name, input.value);
      });
    
      if (hasError) {
        return false;
      }
    
      var textElem = $("#track-scans-text"); // load(thisEl, textElem, "Preparing for track");
    
      olfInputs.forEach(function (input) {
        if (input.name == "custom_logo" && input.value) {
          return formData.append(input.name, input.files[0]);
        }
    
        formData.append(input.name, input.value);
      }); // Checkboxes
    
      $("[name='status']").is(":checked") ? formData.append("status", true) : "";
      $("[name='transparent_code']").is(":checked") ? formData.append("transparent_code", true) : "";
      $("[name='gradient']").is(":checked") ? formData.append("gradient", true) : "";
      $("[name='markers_color']").is(":checked") ? formData.append("markers_color", true) : "";
      $("[name='custom_logo']")[0].files.length > 0 ? formData.append("custom_logo", $("[name='custom_logo']")[0].files[0]) : "";
      $("[name='radial']").is(":checked") ? formData.append("radial", true) : "";
      $("[name='no_logo_bg']").is(":checked") ? formData.append("no_logo_bg", true) : "";
      formData.append("static", true);
      formData.append("gradient_color", $("[name='gradient_color']").val()); // Radios
    
      formData.append("pattern", $("[name='pattern']:checked").val());
      formData.append("marker_out", $("[name='marker_out']:checked").val());
      formData.append("marker_in", $("[name='marker_in']:checked").val());
      formData.append("optionlogo", $("[name='optionlogo']:checked").val());
      formData.append("outer_frame", $("[name='outer_frame']:checked").val()); // Frame
    
      formData.append("framelabel", $("[name='framelabel']").val());
      formData.append("label_font", $("[name='label_font']").val());
      formData.append("type", $("[name='type']:checked").val());
      formData.append("_token", $("meta[name='csrf']").attr("content"));
      $.ajax({
        url: "/qrcode/track/scans",
        type: "POST",
        processData: false,
        contentType: false,
        data: formData,
        success: function success() {
          window.location.href = "/";
        },
        error: function error(_error3) {
          stopLoad(thisEl, textElem, "Track number of scans");
    
          if (_error3.status == 401) {
            window.location.href = "/login";
          }
        },
        xhr: function xhr() {
          var xhr = new window.XMLHttpRequest();
          xhr.upload.addEventListener("progress", function (evt) {
            if (evt.lengthComputable) {
              var percentComplete = evt.loaded / evt.total;
              $("#create-progress").css("width", percentComplete * 100 + "%");
            }
          }, false);
          return xhr;
        }
      });
    }
    
    $("#track-scans").on("click", function () {
      trackScans($(this));
    });
    $(GENERATE_QR_CODE_BTN_ID).on("click", function () {
      trackScans($(this));
    });
    $("#save-qrcode").on("click", function () {
      if ((0,_utilities__WEBPACK_IMPORTED_MODULE_0__.isPureDynamic)($("[name='type']:checked").val())) {
        trackScans($(this));
      } else {
        saveQrCode($(this));
      }
    });
    processSaveQrCode();
    })();
    
    /******/ })()
    ;