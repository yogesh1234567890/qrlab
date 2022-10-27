function sendData(data) {
  const XHR = new XMLHttpRequest();

  const urlEncodedDataPairs = [];

  // Turn the data object into an array of URL-encoded key/value pairs.
  for (const [name, value] of Object.entries(data)) {
    //dont push socialLinks
    if (name !== "socialLinks") {
      urlEncodedDataPairs.push(
        `${encodeURIComponent(name)}=${encodeURIComponent(value)}`,
      );
    }
  }

  //socialLinks is an array of objects with name and url properties 
  //so we need to convert it to a string
  const socialLinks = JSON.stringify(data.socialLinks);
  //add the socialLinks string to the urlEncodedDataPairs array
  urlEncodedDataPairs.push(
    `${encodeURIComponent('socialLinks')}=${encodeURIComponent(socialLinks)}`,
  );


  // Combine the pairs into a single string and replace all %-encoded spaces to
  // the '+' character; matches the behavior of browser form submissions.
  const urlEncodedData = urlEncodedDataPairs.join("&").replace(/%20/g, "+");

  // Define what happens on successful data submission
  XHR.addEventListener("load", (event) => {
  });

  // Define what happens in case of error
  XHR.addEventListener("error", (event) => {
    alert("Oops! Something went wrong.");
  });

  // Set up our request
  XHR.open("POST", "");

  // redirect based on response
  XHR.onreadystatechange = function () {
    if (XHR.readyState === 4) {
      if (XHR.status === 200) {
        social_id = JSON.parse(XHR.responseText).id;
        window.location.href = "/social-media/" + social_id;
      } else {
        console.log(XHR.responseText);
      }
    }
  };


  // Add the required HTTP header for form data POST requests
  XHR.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  // Finally, send our data.
  XHR.send(urlEncodedData);
}

(function () {
  "use strict";
  var e = {
      8236: function (e, o, t) {
        var l = t(9242),
          n = t(3396);
        const i = { class: "app" },
          a = { class: "main-content" };
        function s(e, o, t, l, s, r) {
          const c = (0, n.up)("Navbar"),
            d = (0, n.up)("MenuCreateForm");
          return (
            (0, n.wg)(),
            (0, n.iD)("div", i, [
              (0, n.Wm)(c),
              (0, n._)("div", a, [(0, n.Wm)(d)]),
            ])
          );
        }
        var r ="https://qrlab.co/create-profile/img/logo.ee696d6e.png";
        const c = { class: "navbar" },
          d = (0, n._)("img", { src: r, alt: "", class: "logo" }, null, -1),
          p = (0, n._)(
            "div",
            { class: "nav" },
            [(0, n._)("a", { href: "https://menulab.com/" }, "Home")],
            -1
          ),
          u = [d, p];
        function m(e, o) {
          return (0, n.wg)(), (0, n.iD)("div", c, u);
        }
        var f = t(89);
        const h = {},
          g = (0, f.Z)(h, [["render", m]]);
        var v = g;
        const w = { class: "menu-create-form" },
          _ = { class: "form" },
          b = { class: "form-content" },
          k = { class: "form-footer" },
          I = (0, n._)("i", { class: "bi bi-arrow-left" }, null, -1),
          y = (0, n._)("span", null, "Back", -1),
          S = [I, y],
          x = ["disabled"],
          M = (0, n._)("span", null, "Next", -1),
          D = [M],
          C = { class: "preview" },
          O = { key: 0, class: "form-complete" };
        function P(e, o, t, l, i, a) {
          const s = (0, n.up)("MenuCreateProgress"),
            r = (0, n.up)("FinishMockup"),
            c = (0, n.up)("SignupForm");
          return (
            (0, n.wg)(),
            (0, n.iD)(
              n.HY,
              null,
              [
                (0, n._)("div", w, [
                  (0, n._)("div", _, [
                    (0, n.Wm)(
                      s,
                      { progress: a.progress, currentStep: i.formIdx[0] },
                      null,
                      8,
                      ["progress", "currentStep"]
                    ),
                    (0, n._)("div", b, [
                      ((0, n.wg)(),
                      (0, n.j4)(
                        n.Ob,
                        null,
                        [
                          ((0, n.wg)(),
                          (0, n.j4)(
                            (0, n.LL)(a.formComponent),
                            {
                              onNext: a.nextSlide,
                              onAllowNext:
                                o[0] || (o[0] = (e) => (i.allowNext = !0)),
                              onDisallowNext:
                                o[1] || (o[1] = (e) => (i.allowNext = !1)),
                              onSkipToSignup: a.skipToSignup,
                            },
                            null,
                            8,
                            ["onNext", "onSkipToSignup"]
                          )),
                        ],
                        1024
                      )),
                    ]),
                    (0, n._)("div", k, [
                      i.formIdx[0] > 0 || i.formIdx[1] > 0
                        ? ((0, n.wg)(),
                          (0, n.iD)(
                            "button",
                            {
                              key: 0,
                              class: "btn txt",
                              onClick:
                                o[2] ||
                                (o[2] = (...e) =>
                                  a.prevSlide && a.prevSlide(...e)),
                            },
                            S
                          ))
                        : (0, n.kq)("", !0),
                      (0, n._)(
                        "button",
                        {
                          disabled: !i.allowNext,
                          class: "btn",
                          onClick:
                            o[3] ||
                            (o[3] = (...e) => a.nextSlide && a.nextSlide(...e)),
                        },
                        D,
                        8,
                        x
                      ),
                      (0, n._)(
                        "button",
                        {
                          disabled: !i.allowNext,
                          class: "btn",
                          onClick: (...e) => {
                            const localData = JSON.parse(
                              localStorage.getItem("vstore_profile-info-v2")
                            );
                            sendData(localData);
                          },
                        },
                        "Submit",
                        8,
                        x
                      ),
                    ]),
                  ]),
                  (0, n._)("div", C, [
                    ((0, n.wg)(), (0, n.j4)((0, n.LL)(a.mockupComponent))),
                  ]),
                ]),
                i.formComplete
                  ? ((0, n.wg)(),
                    (0, n.iD)("div", O, [
                      (0, n.Wm)(
                        r,
                        { onSignup: a.handleSignup, onBack: a.handleBack },
                        null,
                        8,
                        ["onSignup", "onBack"]
                      ),
                      i.showSignupFrom
                        ? ((0, n.wg)(),
                          (0, n.j4)(c, {
                            key: 0,
                            onClose:
                              o[4] || (o[4] = (e) => (i.showSignupFrom = !1)),
                          }))
                        : (0, n.kq)("", !0),
                    ]))
                  : (0, n.kq)("", !0),
              ],
              64
            )
          );
        }
        var U = t(7139);
        const L = { class: "menu-create-progress" },
          $ = { class: "progress-bar" },
          F = { class: "progress-stops" },
          z = { class: "sl" },
          j = { class: "text" };
        function N(e, o, t, l, i, a) {
          return (
            (0, n.wg)(),
            (0, n.iD)("div", L, [
              (0, n._)("div", $, [
                (0, n._)(
                  "div",
                  {
                    class: "progress",
                    style: (0, U.j5)({ width: t.progress + "%" }),
                  },
                  null,
                  4
                ),
              ]),
              (0, n._)("div", F, [
                ((0, n.wg)(!0),
                (0, n.iD)(
                  n.HY,
                  null,
                  (0, n.Ko)(
                    e.progressStops,
                    (e, o) => (
                      (0, n.wg)(),
                      (0, n.iD)(
                        "div",
                        {
                          class: (0, U.C_)([
                            "progress-stop",
                            { active: o <= t.currentStep },
                          ]),
                          key: o,
                        },
                        [
                          (0, n._)("div", z, [
                            (0, n._)("span", null, (0, U.zw)(o + 1), 1),
                            (0, n._)("div", j, (0, U.zw)(e), 1),
                          ]),
                        ],
                        2
                      )
                    )
                  ),
                  128
                )),
              ]),
            ])
          );
        }
        var E = {
          props: ["progress", "currentStep"],
          data: () => ({ progressStops: ["Info", "Social"] }),
        };
        const T = (0, f.Z)(E, [["render", N]]);
        var V = T;
        const W = { class: "modal-wrapper" },
          Z = { class: "modal-content" },
          q = (0, n._)(
            "p",
            { class: "modal-title" },
            "Create a new account",
            -1
          ),
          B = { class: "input-group" },
          R = (0, n._)("label", null, "Email", -1),
          A = { class: "input-group" },
          H = (0, n._)("label", null, "Password", -1),
          J = { class: "input-group" },
          Y = (0, n._)("label", null, "Confirm", -1),
          K = { class: "modal-footer" };
        function G(e, o, t, i, a, s) {
          return (
            (0, n.wg)(),
            (0, n.iD)("div", W, [
              (0, n._)("div", Z, [
                (0, n._)("i", {
                  class: "bi bi-x modal-close",
                  onClick: o[0] || (o[0] = (o) => e.$emit("close")),
                }),
                q,
                (0, n._)("div", B, [
                  R,
                  (0, n.wy)(
                    (0, n._)(
                      "input",
                      {
                        "onUpdate:modelValue":
                          o[1] || (o[1] = (o) => (e.email = o)),
                        type: "text",
                        placeholder: "Type your email address",
                        class: "create-form-input",
                      },
                      null,
                      512
                    ),
                    [[l.nr, e.email]]
                  ),
                ]),
                (0, n._)("div", A, [
                  H,
                  (0, n.wy)(
                    (0, n._)(
                      "input",
                      {
                        "onUpdate:modelValue":
                          o[2] || (o[2] = (o) => (e.password = o)),
                        type: "password",
                        placeholder: "Type your password",
                        class: "create-form-input",
                      },
                      null,
                      512
                    ),
                    [[l.nr, e.password]]
                  ),
                ]),
                (0, n._)("div", J, [
                  Y,
                  (0, n.wy)(
                    (0, n._)(
                      "input",
                      {
                        "onUpdate:modelValue":
                          o[3] || (o[3] = (o) => (e.confirm = o)),
                        type: "password",
                        placeholder: "Confirm your password",
                        class: "create-form-input",
                      },
                      null,
                      512
                    ),
                    [[l.nr, e.confirm]]
                  ),
                ]),
                (0, n._)("div", K, [
                  (0, n._)(
                    "button",
                    {
                      class: "btn txt",
                      onClick: o[4] || (o[4] = (o) => e.$emit("close")),
                    },
                    "Cancel"
                  ),
                  (0, n._)(
                    "button",
                    {
                      class: "btn",
                      onClick:
                        o[5] || (o[5] = (...e) => s.signup && s.signup(...e)),
                    },
                    "Sign up"
                  ),
                ]),
              ]),
            ])
          );
        }
        var Q = {
          data: () => ({ email: "", password: "", confirm: "" }),
          methods: {
            signup() {
              this.$toast.success("Registration complete"), this.$emit("close");
            },
          },
        };
        const X = (0, f.Z)(Q, [["render", G]]);
        var ee = X;
        const oe = (0, n._)(
            "p",
            { class: "title" },
            "Provide you personal information",
            -1
          ),
          te = { class: "input-group" },
          le = (0, n._)("label", null, "Profile picture", -1),
          ne = { class: "input-group" },
          ie = (0, n._)("label", null, "Full Name", -1),
          ae = { class: "input-group" },
          se = (0, n._)("label", null, "Title", -1),
          re = { class: "input-group" },
          ce = (0, n._)("label", null, "Email", -1),
          de = { class: "input-group" },
          pe = (0, n._)("label", null, "Phone", -1),
          ue = { class: "input-group" },
          me = (0, n._)("label", null, "Website", -1);
        function fe(e, o, t, i, a, s) {
          const r = (0, n.up)("ImgUpload");
          return (
            (0, n.wg)(),
            (0, n.iD)("div", null, [
              oe,
              (0, n._)("div", te, [
                le,
                (0, n.Wm)(
                  r,
                  { onResult: s.handleImg, maxSize: 200, defaultImg: a.dp },
                  null,
                  8,
                  ["onResult", "defaultImg"]
                ),
              ]),
              (0, n._)("div", ne, [
                ie,
                (0, n.wy)(
                  (0, n._)(
                    "input",
                    {
                      type: "text",
                      placeholder: "Enter your name",
                      "onUpdate:modelValue":
                        o[0] || (o[0] = (e) => (a.info.name = e)),
                    },
                    null,
                    512
                  ),
                  [[l.nr, a.info.name]]
                ),
              ]),
              (0, n._)("div", ae, [
                se,
                (0, n.wy)(
                  (0, n._)(
                    "input",
                    {
                      type: "text",
                      placeholder: "Enter your title",
                      "onUpdate:modelValue":
                        o[1] || (o[1] = (e) => (a.info.title = e)),
                    },
                    null,
                    512
                  ),
                  [[l.nr, a.info.title]]
                ),
              ]),
              (0, n._)("div", re, [
                ce,
                (0, n.wy)(
                  (0, n._)(
                    "input",
                    {
                      type: "email",
                      placeholder: "Enter your email",
                      "onUpdate:modelValue":
                        o[2] || (o[2] = (e) => (a.info.email = e)),
                    },
                    null,
                    512
                  ),
                  [[l.nr, a.info.email]]
                ),
              ]),
              (0, n._)("div", de, [
                pe,
                (0, n.wy)(
                  (0, n._)(
                    "input",
                    {
                      type: "text",
                      placeholder: "Enter your phone number",
                      "onUpdate:modelValue":
                        o[3] || (o[3] = (e) => (a.info.phone = e)),
                    },
                    null,
                    512
                  ),
                  [[l.nr, a.info.phone]]
                ),
              ]),
              (0, n._)("div", ue, [
                me,
                (0, n.wy)(
                  (0, n._)(
                    "input",
                    {
                      type: "url",
                      placeholder: "Enter your website URL",
                      "onUpdate:modelValue":
                        o[4] || (o[4] = (e) => (a.info.website = e)),
                    },
                    null,
                    512
                  ),
                  [[l.nr, a.info.website]]
                ),
              ]),
            ])
          );
        }
        const he = (e) => (
            (0, n.dD)("data-v-ac020f7a"), (e = e()), (0, n.Cn)(), e
          ),
          ge = { key: 0, class: "img-drop-preview" },
          ve = ["src"],
          we = { class: "img-drop-preview__remove" },
          _e = he(() =>
            (0, n._)("i", { class: "bi bi-cloud-arrow-up" }, null, -1)
          ),
          be = he(() =>
            (0, n._)("span", null, "Drag and drop files here or browse", -1)
          );
        function ke(e, o, t, l, i, a) {
          return i.img
            ? ((0, n.wg)(),
              (0, n.iD)("div", ge, [
                (0, n._)("img", { src: i.img, alt: "" }, null, 8, ve),
                (0, n._)("div", we, [
                  (0, n._)("i", {
                    class: "bi bi-trash",
                    onClick:
                      o[0] ||
                      (o[0] = (...e) => a.removeImg && a.removeImg(...e)),
                  }),
                ]),
              ]))
            : ((0, n.wg)(),
              (0, n.iD)(
                "label",
                {
                  key: 1,
                  onDragenter:
                    o[2] ||
                    (o[2] = (...e) =>
                      a.handleDragEnter && a.handleDragEnter(...e)),
                  onDragleave:
                    o[3] ||
                    (o[3] = (...e) =>
                      a.handleDragLeave && a.handleDragLeave(...e)),
                  onDragover:
                    o[4] ||
                    (o[4] = (...e) =>
                      a.handleDragOver && a.handleDragOver(...e)),
                  onDrop:
                    o[5] ||
                    (o[5] = (...e) => a.handleDrop && a.handleDrop(...e)),
                  class: "img-drop-zone",
                  for: "customImg",
                  ref: "dropZone",
                },
                [
                  _e,
                  be,
                  (0, n._)(
                    "input",
                    {
                      onChange:
                        o[1] ||
                        (o[1] = (...e) =>
                          a.handleChange && a.handleChange(...e)),
                      type: "file",
                      name: "customImg",
                      id: "customImg",
                    },
                    null,
                    32
                  ),
                ],
                544
              ));
        }
        var Ie = {
          props: ["defaultImg", "maxSize"],
          data() {
            let e = this.defaultImg || "";
            return { img: e };
          },
          methods: {
            handleDragEnter(e) {
              e.preventDefault(), e.stopPropagation();
            },
            handleDragLeave(e) {
              e.preventDefault(), e.stopPropagation();
            },
            handleDragOver(e) {
              e.preventDefault(), e.stopPropagation();
            },
            handleDrop(e) {
              e.preventDefault(),
                e.stopPropagation(),
                e.dataTransfer.files.length &&
                  this.handeImg(e.dataTransfer.files[0]);
            },
            handleChange(e) {
              e.target.files.length && this.handeImg(e.target.files[0]);
            },
            handeImg(e) {
              if (-1 === e.type.indexOf("image"))
                return alert("Please upload an image");
              if (e.size < 5e3)
                return alert("Please upload an image larger than 5kb");
              if (e.size > 5e6)
                return alert("Please upload an image less than 5mb");
              const o = new FileReader();
              (o.onload = () => {
                if (!this.maxSize)
                  return (
                    (this.img = o.result), void this.$emit("result", o.result)
                  );
                const e = new Image();
                (e.src = o.result),
                  (e.onload = () => {
                    console.log("start");
                    const o = document.createElement("canvas"),
                      t = this.maxSize;
                    let l = e.width,
                      n = e.height;
                    l > n
                      ? l > t && ((n *= t / l), (l = t))
                      : n > t && ((l *= t / n), (n = t)),
                      (o.width = l),
                      (o.height = n),
                      o.getContext("2d").drawImage(e, 0, 0, l, n);
                    const i = o.toDataURL("image/png");
                    (this.img = i), this.$emit("result", i);
                  });
              }),
                o.readAsDataURL(e);
            },
            removeImg() {
              (this.img = ""), this.$emit("result", "");
            },
          },
        };
        const ye = (0, f.Z)(Ie, [
          ["render", ke],
          ["__scopeId", "data-v-ac020f7a"],
        ]);
        var Se = ye,
          xe = {
            components: { ImgUpload: Se },
            data() {
              const e = { ...this.$store.state.profileInfo };
              return {
                dp: e.dp,
                info: {
                  name: e.name,
                  title: e.title,
                  email: e.email,
                  phone: e.phone,
                  website: e.website,
                },
              };
            },
            methods: {
              handleImg(e) {
                this.$store.state.profileInfo.dp = e;
              },
            },
            watch: {
              info: {
                handler(e) {
                  (this.$store.state.profileInfo.name = e.name),
                    (this.$store.state.profileInfo.title = e.title),
                    (this.$store.state.profileInfo.email = e.email),
                    (this.$store.state.profileInfo.phone = e.phone),
                    (this.$store.state.profileInfo.website = e.website);
                },
                deep: !0,
              },
            },
          };
        const Me = (0, f.Z)(xe, [["render", fe]]);
        var De = Me;
        const Ce = (0, n._)(
            "p",
            { class: "title" },
            "Provide you social links",
            -1
          ),
          Oe = { class: "user-socials user-socials-preview" },
          Pe = ["src"],
          Ue = { class: "text" },
          Le = ["onClick"],
          $e = (0, n._)(
            "span",
            { class: "sort-icon handle" },
            [
              (0, n._)("i", { class: "bi bi-three-dots-vertical" }),
              (0, n._)("i", { class: "bi bi-three-dots-vertical" }),
            ],
            -1
          ),
          Fe = { class: "input-group" },
          ze = (0, n._)("label", null, "Select social media", -1),
          je = { class: "select-wrapper" },
          Ne = ["value"],
          Ee = (0, n._)("option", { value: "other" }, "Other", -1),
          Te = { class: "input-group" },
          Ve = { class: "input-group" },
          We = (0, n._)("label", null, "Add link", -1),
          Ze = { key: 0, class: "input-group" },
          qe = (0, n._)("label", null, "Social media logo(Optional)", -1),
          Be = ["disabled"];
        function Re(e, o, t, i, a, s) {
          const r = (0, n.up)("draggable"),
            c = (0, n.up)("ImgUpload");
          return (
            (0, n.wg)(),
            (0, n.iD)("div", null, [
              Ce,
              (0, n._)("div", Oe, [
                (0, n.Wm)(
                  r,
                  {
                    modelValue: a.socials,
                    "onUpdate:modelValue":
                      o[0] || (o[0] = (e) => (a.socials = e)),
                    handle: ".handle",
                  },
                  {
                    item: (0, n.w5)(({ element: e, index: o }) => [
                      (0, n.wy)(
                        (0, n._)(
                          "div",
                          {
                            style: (0, U.j5)({
                              "--animate-delay": 0.15 * o + "s",
                            }),
                            class: "user-social",
                          },
                          [
                            e.imgIcon
                              ? ((0, n.wg)(),
                                (0, n.iD)(
                                  "img",
                                  {
                                    key: 0,
                                    src: e.icon,
                                    alt: "",
                                    class: "icon",
                                  },
                                  null,
                                  8,
                                  Pe
                                ))
                              : ((0, n.wg)(),
                                (0, n.iD)(
                                  "i",
                                  {
                                    key: 1,
                                    class: (0, U.C_)("icon bi bi-" + e.icon),
                                  },
                                  null,
                                  2
                                )),
                            (0, n._)("span", Ue, (0, U.zw)(e.title), 1),
                            (0, n._)(
                              "i",
                              {
                                class: "bi bi-trash",
                                onClick: (e) => s.deleteSocial(o),
                              },
                              null,
                              8,
                              Le
                            ),
                            $e,
                          ],
                          4
                        ),
                        [[l.F8, e.link]]
                      ),
                    ]),
                    _: 1,
                  },
                  8,
                  ["modelValue"]
                ),
              ]),
              (0, n._)(
                "form",
                {
                  onSubmit:
                    o[4] ||
                    (o[4] = (0, l.iM)(
                      (...e) => s.addSocial && s.addSocial(...e),
                      ["prevent"]
                    )),
                  to: "?",
                  method: "post",
                  class: "social-link-add-form",
                },
                [
                  (0, n._)("div", Fe, [
                    ze,
                    (0, n._)("div", je, [
                      (0, n.wy)(
                        (0, n._)(
                          "select",
                          {
                            "onUpdate:modelValue":
                              o[1] ||
                              (o[1] = (e) => (a.socialMedialModel.media = e)),
                          },
                          [
                            ((0, n.wg)(!0),
                            (0, n.iD)(
                              n.HY,
                              null,
                              (0, n.Ko)(
                                a.socialLinkFields,
                                (e, o) => (
                                  (0, n.wg)(),
                                  (0, n.iD)(
                                    "option",
                                    {
                                      key: o,
                                      value: e,
                                      class: "text-capitalize",
                                    },
                                    (0, U.zw)(e),
                                    9,
                                    Ne
                                  )
                                )
                              ),
                              128
                            )),
                            Ee,
                          ],
                          512
                        ),
                        [[l.bM, a.socialMedialModel.media]]
                      ),
                    ]),
                  ]),
                  (0, n._)("div", Te, [
                    (0, n._)(
                      "label",
                      null,
                      "Label " +
                        (0, U.zw)(
                          "other" !== a.socialMedialModel.media
                            ? "(Optional)"
                            : ""
                        ),
                      1
                    ),
                    (0, n.wy)(
                      (0, n._)(
                        "input",
                        {
                          type: "text",
                          placeholder: "Social media label",
                          "onUpdate:modelValue":
                            o[2] ||
                            (o[2] = (e) => (a.socialMedialModel.label = e)),
                        },
                        null,
                        512
                      ),
                      [[l.nr, a.socialMedialModel.label]]
                    ),
                  ]),
                  (0, n._)("div", Ve, [
                    We,
                    (0, n.wy)(
                      (0, n._)(
                        "input",
                        {
                          type: "text",
                          placeholder: "Enter link to social media",
                          "onUpdate:modelValue":
                            o[3] ||
                            (o[3] = (e) => (a.socialMedialModel.link = e)),
                        },
                        null,
                        512
                      ),
                      [[l.nr, a.socialMedialModel.link]]
                    ),
                  ]),
                  "other" === a.socialMedialModel.media
                    ? ((0, n.wg)(),
                      (0, n.iD)("div", Ze, [
                        qe,
                        (0, n.Wm)(
                          c,
                          { maxSize: 80, onResult: s.handleImg },
                          null,
                          8,
                          ["onResult"]
                        ),
                      ]))
                    : (0, n.kq)("", !0),
                  (0, n._)(
                    "button",
                    {
                      class: "btn square",
                      type: "submit",
                      disabled:
                        !a.socialMedialModel.media.trim() ||
                        !a.socialMedialModel.link.trim(),
                    },
                    "Add Social Media",
                    8,
                    Be
                  ),
                ],
                32
              ),
            ])
          );
        }
        var Ae = t(6983),
          He = t.n(Ae);
        const Je = [
          "facebook",
          "twitter",
          "instagram",
          "linkedin",
          "pinterest",
          "youtube",
          "snapchat",
          "reddit",
        ];
        var Ye = {
          components: { ImgUpload: Se, draggable: He() },
          data() {
            let e = [];
            const o = this.$store.state.profileInfo.socialLinks;
            return (
              console.log(o),
              o && o.length > 0 && (e = JSON.parse(JSON.stringify(o))),
              {
                socialLinkFields: Je,
                socials: e,
                socialMedialModel: {
                  media: "facebook",
                  label: "",
                  link: "",
                  icon: "",
                },
                socialMedialOtherLogo: "",
              }
            );
          },
          methods: {
            addSocial() {
              if (Je.includes(this.socialMedialModel.media))
                this.socials.push({
                  title:
                    this.socialMedialModel.label ||
                    this.socialMedialModel.media,
                  icon: this.socialMedialModel.media,
                  link: this.socialMedialModel.link,
                });
              else {
                const e = {
                  title: this.socialMedialModel.label,
                  link: this.socialMedialModel.link,
                };
                this.socialMedialOtherLogo
                  ? ((e.icon = this.socialMedialOtherLogo), (e.imgIcon = !0))
                  : (e.icon = "globe"),
                  this.socials.push(e),
                  (this.socialMedialOtherLogo = "");
              }
              this.socialMedialModel = {
                media: "facebook",
                label: "",
                link: "",
                icon: "",
              };
            },
            handleImg(e) {
              this.socialMedialOtherLogo = e;
            },
            deleteSocial(e) {
              this.socials.splice(e, 1);
            },
          },
          watch: {
            socials: {
              handler(e) {
                this.$store.state.profileInfo.socialLinks = e;
              },
              deep: !0,
            },
          },
        };
        const Ke = (0, f.Z)(Ye, [["render", Re]]);
        var Ge = Ke;
        const Qe = { class: "finished-mockup-wrapper" },
          Xe = { class: "phone-screen-main finished-mockup" },
          eo = { class: "finished-cta-wrapper" },
          oo = (0, n._)("h2", null, "Your profile is ready!", -1),
          to = (0, n._)("p", null, "Sign up to start using it", -1),
          lo = (0, n._)(
            "p",
            null,
            [
              (0, n._)(
                "a",
                { href: "https://menulab.com", class: "btn" },
                "Sign Up"
              ),
            ],
            -1
          ),
          no = (0, n._)("p", { class: "mt-1" }, "or", -1),
          io = (0, n._)("u", null, "Back to edit", -1),
          ao = [io];
        function so(e, o, t, l, i, a) {
          const s = (0, n.up)("ProfileMockupConetnt"),
            r = (0, n.up)("PhoneMockUp");
          return (
            (0, n.wg)(),
            (0, n.iD)("div", Qe, [
              (0, n.Wm)(r, null, {
                default: (0, n.w5)(() => [
                  (0, n._)("div", Xe, [
                    (0, n.Wm)(s),
                    (0, n._)("div", eo, [
                      (0, n._)("div", null, [
                        oo,
                        to,
                        lo,
                        no,
                        (0, n._)("p", null, [
                          (0, n._)(
                            "button",
                            {
                              onClick:
                                o[0] ||
                                (o[0] = (...e) =>
                                  a.handleBack && a.handleBack(...e)),
                              class: "btn bg-none pt-0",
                            },
                            ao
                          ),
                        ]),
                      ]),
                    ]),
                  ]),
                ]),
                _: 1,
              }),
            ])
          );
        }
        var ro ="https://qrlab.co/create-profile/img/mockup-phone.d859e481.png";
        const co = { class: "phone-mockup-container" },
          po = { class: "phone-mockup-phone" },
          uo = { class: "phone-mockup-content" },
          mo = (0, n._)(
            "img",
            { src: ro, alt: "", class: "phone-mockup-phone-img" },
            null,
            -1
          );
        function fo(e, o) {
          return (
            (0, n.wg)(),
            (0, n.iD)("div", co, [
              (0, n._)("div", po, [
                (0, n._)("div", uo, [(0, n.WI)(e.$slots, "default")]),
                mo,
              ]),
            ])
          );
        }
        const ho = {},
          go = (0, f.Z)(ho, [["render", fo]]);
        var vo = go;
        const wo = (e) => (
            (0, n.dD)("data-v-69f60277"), (e = e()), (0, n.Cn)(), e
          ),
          _o = { class: "mockup-content-container" },
          bo = ["src"],
          ko = { key: 1, class: "user-name" },
          Io = { class: "user-infos" },
          yo = { key: 0 },
          So = wo(() => (0, n._)("span", null, "title:", -1)),
          xo = (0, n.Uk)(),
          Mo = { key: 1 },
          Do = wo(() => (0, n._)("span", null, "email:", -1)),
          Co = (0, n.Uk)(),
          Oo = { key: 2 },
          Po = wo(() => (0, n._)("span", null, "phone:", -1)),
          Uo = (0, n.Uk)(),
          Lo = { key: 3 },
          $o = wo(() => (0, n._)("span", null, "website:", -1)),
          Fo = (0, n.Uk)(),
          zo = ["href"],
          jo = ["href"],
          No = ["src"],
          Eo = { class: "text" };
        function To(e, o, t, i, a, s) {
          return (
            (0, n.wg)(),
            (0, n.iD)("div", _o, [
              s.profileInfo.dp
                ? ((0, n.wg)(),
                  (0, n.iD)(
                    "img",
                    {
                      key: 0,
                      style: (0, U.j5)({ "--dp-border": a.dpBorder }),
                      src: s.profileInfo.dp,
                      alt: "",
                      class: "user-dp",
                    },
                    null,
                    12,
                    bo
                  ))
                : (0, n.kq)("", !0),
              s.profileInfo.name
                ? ((0, n.wg)(),
                  (0, n.iD)("p", ko, (0, U.zw)(s.profileInfo.name), 1))
                : (0, n.kq)("", !0),
              (0, n._)("div", Io, [
                s.profileInfo.title
                  ? ((0, n.wg)(),
                    (0, n.iD)("p", yo, [
                      So,
                      xo,
                      (0, n._)("span", null, (0, U.zw)(s.profileInfo.title), 1),
                    ]))
                  : (0, n.kq)("", !0),
                s.profileInfo.email
                  ? ((0, n.wg)(),
                    (0, n.iD)("p", Mo, [
                      Do,
                      Co,
                      (0, n._)("span", null, (0, U.zw)(s.profileInfo.email), 1),
                    ]))
                  : (0, n.kq)("", !0),
                s.profileInfo.phone
                  ? ((0, n.wg)(),
                    (0, n.iD)("p", Oo, [
                      Po,
                      Uo,
                      (0, n._)("span", null, (0, U.zw)(s.profileInfo.phone), 1),
                    ]))
                  : (0, n.kq)("", !0),
                s.profileInfo.website
                  ? ((0, n.wg)(),
                    (0, n.iD)("p", Lo, [
                      $o,
                      Fo,
                      (0, n._)("span", null, [
                        (0, n._)(
                          "a",
                          {
                            target: "_blank",
                            href: s.profileInfo.website
                              ? s.getLink(s.profileInfo.website)
                              : "#",
                          },
                          (0, U.zw)(s.profileInfo.website),
                          9,
                          zo
                        ),
                      ]),
                    ]))
                  : (0, n.kq)("", !0),
              ]),
              (0, n._)(
                "div",
                {
                  class: "user-socials",
                  style: (0, U.j5)({ "--list-color": a.listColor }),
                },
                [
                  ((0, n.wg)(!0),
                  (0, n.iD)(
                    n.HY,
                    null,
                    (0, n.Ko)(s.profileInfo.socialLinks, (e, o) =>
                      (0, n.wy)(
                        ((0, n.wg)(),
                        (0, n.iD)(
                          "a",
                          {
                            key: o,
                            href: s.getLink(e.link),
                            style: (0, U.j5)({
                              "--animate-delay": 0.15 * o + "s",
                            }),
                            class: "user-social",
                            target: "_blank",
                          },
                          [
                            e.imgIcon
                              ? ((0, n.wg)(),
                                (0, n.iD)(
                                  "img",
                                  {
                                    key: 0,
                                    src: e.icon,
                                    alt: "",
                                    class: "icon",
                                  },
                                  null,
                                  8,
                                  No
                                ))
                              : ((0, n.wg)(),
                                (0, n.iD)(
                                  "i",
                                  {
                                    key: 1,
                                    class: (0, U.C_)("icon bi bi-" + e.icon),
                                  },
                                  null,
                                  2
                                )),
                            (0, n._)("span", Eo, (0, U.zw)(e.title), 1),
                          ],
                          12,
                          jo
                        )),
                        [[l.F8, e.link]]
                      )
                    ),
                    128
                  )),
                ],
                4
              ),
            ])
          );
        }
        var Vo = {
          data() {
            return {
              dpBorder: "rgb(114, 73, 54)",
              listColor: "#fff",
              bgColor: "#fff",
            };
          },
          computed: {
            profileInfo() {
              return this.$store.state.profileInfo;
            },
          },
          methods: {
            getLink(e) {
              return e.startsWith("http") ? e : "http://" + e;
            },
          },
          mounted() {
            document.body.style.backgroundColor = this.bgColor;
          },
        };
        const Wo = (0, f.Z)(Vo, [
          ["render", To],
          ["__scopeId", "data-v-69f60277"],
        ]);
        var Zo = Wo,
          qo = {
            components: { PhoneMockUp: vo, ProfileMockupConetnt: Zo },
            methods: {
              handleBack() {
                this.$emit("back");
              },
            },
          };
        const Bo = (0, f.Z)(qo, [["render", so]]);
        var Ro = Bo;
        const Ao = { class: "phone-screen-main" },
          Ho = (0, n._)(
            "div",
            { class: "phone-navbar" },
            [(0, n._)("img", { src: r, alt: "", class: "logo" })],
            -1
          ),
          Jo = { class: "phone-content" };
        function Yo(e, o, t, l, i, a) {
          const s = (0, n.up)("ProfileMockupConetnt"),
            r = (0, n.up)("PhoneMockUp");
          return (
            (0, n.wg)(),
            (0, n.j4)(r, null, {
              default: (0, n.w5)(() => [
                (0, n._)("div", Ao, [Ho, (0, n._)("div", Jo, [(0, n.Wm)(s)])]),
              ]),
              _: 1,
            })
          );
        }
        var Ko = { components: { PhoneMockUp: vo, ProfileMockupConetnt: Zo } };
        const Go = (0, f.Z)(Ko, [["render", Yo]]);
        var Qo = Go;
        function Xo(e, o, t, l, n) {
          return ((e - o) * (n - l)) / (t - o) + l;
        }
        var et = {
          components: {
            MenuCreateProgress: V,
            FinishMockup: Ro,
            SignupForm: ee,
          },
          data() {
            const e = this.$store.state.profileInfo.formIdx;
            return {
              showSignupFrom: !1,
              forms: [[De, Ge]],
              mockups: [[Qo, Qo]],
              formIdx: e || [0, 0],
              allowNext: !0,
              formComplete: !1,
            };
          },
          watch: {
            formIdx: {
              handler(e) {
                this.$store.state.profileInfo.formIdx = e;
              },
              deep: !0,
            },
          },
          methods: {
            nextSlide() {
              let e = this.formIdx[0],
                o = this.formIdx[1];
              o < this.forms[e].length - 1
                ? this.formIdx[1]++
                : e < this.forms.length - 1
                ? (this.formIdx[0]++, (this.formIdx[1] = 0))
                : (this.formComplete = !0);
            },
            prevSlide() {
              this.allowNext = !0;
              let e = this.formIdx[0],
                o = this.formIdx[1];
              o > 0
                ? this.formIdx[1]--
                : e > 0 &&
                  (this.formIdx[0]--,
                  (this.formIdx[1] = this.forms[e - 1].length - 1));
            },
            skipToSignup() {
              this.formComplete = !0;
            },
            handleSignup() {
              this.showSignupFrom = !0;
            },
            handleBack() {
              this.formComplete = !1;
            },
          },
          computed: {
            progress() {
              let e = this.formIdx[0],
                o = this.formIdx[1];
              if (e == this.forms.length - 1 && o == this.forms[e].length - 1)
                return 100;
              let t = 33.33 * e,
                l = Xo(o, 0, this.forms[e].length - 1, 0, 33.33);
              return t + l;
            },
            formComponent() {
              return this.forms[this.formIdx[0]][this.formIdx[1]];
            },
            mockupComponent() {
              return this.mockups[this.formIdx[0]][this.formIdx[1]];
            },
          },
        };
        const ot = (0, f.Z)(et, [["render", P]]);
        var tt = ot,
          lt = JSON.parse(
            '[{"titles":["Roboto","Arial"],"fonts":["\'Roboto\'","Arial"]},{"titles":["Dancing Script","Sansita"],"fonts":["\'Dancing Script\'","Sansita"]},{"titles":["Allerta","Allerta"],"fonts":["\'Allerta\'","\'Allerta\'"]},{"titles":["Candal","Candal"],"fonts":["\'Candal\'","\'Candal\'"]},{"titles":["Fredoka","Fredoka"],"fonts":["\'Fredoka\'","\'Fredoka\'"]},{"titles":["Solway","Solway"],"fonts":["\'Solway\'","\'Solway\'"]}]'
          ),
          nt = {
            components: { Navbar: v, MenuCreateForm: tt },
            created() {
              this.$store.commit("loadProfileInfo");
            },
            mounted() {
              const e = this.$store.state.profileInfo.fonts;
              if (!e) return;
              const o = lt.find((o) => o.fonts[1] == e);
              o &&
                document.documentElement.style.setProperty(
                  "--preview-font",
                  o.fonts[0]
                );
            },
            watch: {
              "$store.state.profileInfo": {
                handler() {
                  this.$store.commit("saveProfileInfo");
                },
                deep: !0,
              },
            },
          };
        const it = (0, f.Z)(nt, [["render", s]]);
        var at = it,
          st = t(65);
        const rt = "vstore_profile-info-v2";
        var ct = (0, st.MT)({
          state: {
            profileInfo: {
              dp: "",
              name: "",
              title: "",
              email: "",
              phone: "",
              socialLinks: [],
              website: "",
              formIdx: [0, 0],
            },
          },
          getters: {},
          mutations: {
            saveProfileInfo(e) {
              localStorage.setItem(rt, JSON.stringify(e.profileInfo));
            },
            loadProfileInfo(e) {
              const o = JSON.parse(localStorage.getItem(rt));
              o && (e.profileInfo = o);
            },
          },
          actions: {},
          modules: {},
        });
        (0, l.ri)(at).use(ct).mount("#app");
      },
    },
    o = {};
  function t(l) {
    var n = o[l];
    if (void 0 !== n) return n.exports;
    var i = (o[l] = { exports: {} });
    return e[l].call(i.exports, i, i.exports, t), i.exports;
  }
  (t.m = e),
    (function () {
      var e = [];
      t.O = function (o, l, n, i) {
        if (!l) {
          var a = 1 / 0;
          for (d = 0; d < e.length; d++) {
            (l = e[d][0]), (n = e[d][1]), (i = e[d][2]);
            for (var s = !0, r = 0; r < l.length; r++)
              (!1 & i || a >= i) &&
              Object.keys(t.O).every(function (e) {
                return t.O[e](l[r]);
              })
                ? l.splice(r--, 1)
                : ((s = !1), i < a && (a = i));
            if (s) {
              e.splice(d--, 1);
              var c = n();
              void 0 !== c && (o = c);
            }
          }
          return o;
        }
        i = i || 0;
        for (var d = e.length; d > 0 && e[d - 1][2] > i; d--) e[d] = e[d - 1];
        e[d] = [l, n, i];
      };
    })(),
    (function () {
      t.n = function (e) {
        var o =
          e && e.__esModule
            ? function () {
                return e["default"];
              }
            : function () {
                return e;
              };
        return t.d(o, { a: o }), o;
      };
    })(),
    (function () {
      t.d = function (e, o) {
        for (var l in o)
          t.o(o, l) &&
            !t.o(e, l) &&
            Object.defineProperty(e, l, { enumerable: !0, get: o[l] });
      };
    })(),
    (function () {
      t.g = (function () {
        if ("object" === typeof globalThis) return globalThis;
        try {
          return this || new Function("return this")();
        } catch (e) {
          if ("object" === typeof window) return window;
        }
      })();
    })(),
    (function () {
      t.o = function (e, o) {
        return Object.prototype.hasOwnProperty.call(e, o);
      };
    })(),
    (function () {
      t.r = function (e) {
        "undefined" !== typeof Symbol &&
          Symbol.toStringTag &&
          Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
          Object.defineProperty(e, "__esModule", { value: !0 });
      };
    })(),
    (function () {
      t.p = "/create-profile/";
    })(),
    (function () {
      var e = { 143: 0 };
      t.O.j = function (o) {
        return 0 === e[o];
      };
      var o = function (o, l) {
          var n,
            i,
            a = l[0],
            s = l[1],
            r = l[2],
            c = 0;
          if (
            a.some(function (o) {
              return 0 !== e[o];
            })
          ) {
            for (n in s) t.o(s, n) && (t.m[n] = s[n]);
            if (r) var d = r(t);
          }
          for (o && o(l); c < a.length; c++)
            (i = a[c]), t.o(e, i) && e[i] && e[i][0](), (e[i] = 0);
          return t.O(d);
        },
        l = (self["webpackChunkmenu_creator"] =
          self["webpackChunkmenu_creator"] || []);
      l.forEach(o.bind(null, 0)), (l.push = o.bind(null, l.push.bind(l)));
    })();
  var l = t.O(void 0, [998], function () {
    return t(8236);
  });
  l = t.O(l);
})();
//# sourceMappingURL=app.ef3ac9d7.js.map
