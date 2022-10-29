(function () {
  "use strict";
  var t = {
      9518: function (t, n, e) {
        var i = e(6369),
          o = function () {
            var t = this,
              n = t._self._c;
            return n("div", { staticClass: "container" }, [
              n("img", {
                staticClass: "user-dp",
                style: { "--dp-border": t.dpBorder },
                attrs: { src: t.dp, alt: "" },
              }),
              n("p", { staticClass: "user-name" }, [t._v(t._s(t.name))]),
              n("div", { staticClass: "user-infos" }, [
                n("p", [
                  n("span", [t._v("title:")]),
                  t._v(" "),
                  n("span", [t._v(t._s(t.title))]),
                ]),
                n("p", [
                  n("span", [t._v("email:")]),
                  t._v(" "),
                  n("span", [t._v(t._s(t.email))]),
                ]),
                n("p", [
                  n("span", [t._v("phone:")]),
                  t._v(" "),
                  n("span", [t._v(t._s(t.phone))]),
                ]),
                n("p", [
                  n("span", [t._v("website:")]),
                  t._v(" "),
                  n("span", [
                    n("a", { attrs: { href: "#" } }, [t._v(t._s(t.website))]),
                  ]),
                ]),
              ]),
              n(
                "div",
                {
                  staticClass: "user-socials",
                  style: { "--list-color": t.listColor },
                },
                t._l(t.socials, function (e, i) {
                  return n(
                    "a",
                    {
                      key: i,
                      staticClass: "user-social",
                      style: { "--animate-delay": 0.15 * i + "s" },
                      attrs: { href: e.link },
                    },
                    [
                      n("i", { class: "icon bi bi-" + e.icon }),
                      n("span", { staticClass: "text" }, [t._v(t._s(e.title))]),
                      t._m(0, !0),
                    ]
                  );
                }),
                0
              ),
            ]);
          },
          r = [
            function () {
              var t = this,
                n = t._self._c;
              return n("span", { staticClass: "visit-btn" }, [
                n("i", { staticClass: "bi bi-box-arrow-right" }),
              ]);
            },
          ],
          s = "https://qrlab.co/profile/img/dp.d2c0a9c3.png",
          a = {
            data() {
              return {
                dp: s,
                name: "Selena Gomez",
                title: "Singer/Artist",
                email: "selenagomez@gmail.com",
                phone: "+1-202-555-0148",
                website: "selenagomez.com",
                socials: [
                  { title: "facebook", icon: "facebook", link: "menulab.com" },
                  { title: "twitter", icon: "twitter", link: "menulab.com" },
                  {
                    title: "instagram",
                    icon: "instagram",
                    link: "menulab.com",
                  },
                  { title: "linkedin", icon: "linkedin", link: "menulab.com" },
                  {
                    title: "pinterest",
                    icon: "pinterest",
                    link: "menulab.com",
                  },
                  { title: "youtube", icon: "youtube", link: "menulab.com" },
                  { title: "snapchat", icon: "snapchat", link: "menulab.com" },
                  { title: "reddit", icon: "reddit", link: "menulab.com" },
                ],
                dpBorder: "rgb(114, 73, 54)",
                listColor: "#fff",
                bgColor: "#fff",
              };
            },
            mounted() {
              document.body.style.backgroundColor = this.bgColor;
            },
          },
          l = a,
          c = e(1001),
          u = (0, c.Z)(l, o, r, !1, null, null, null),
          f = u.exports;
        (i.ZP.config.productionTip = !1),
          new i.ZP({ render: (t) => t(f) }).$mount("#app");
      },
    },
    n = {};
  function e(i) {
    var o = n[i];
    if (void 0 !== o) return o.exports;
    var r = (n[i] = { exports: {} });
    return t[i](r, r.exports, e), r.exports;
  }
  (e.m = t),
    (function () {
      var t = [];
      e.O = function (n, i, o, r) {
        if (!i) {
          var s = 1 / 0;
          for (u = 0; u < t.length; u++) {
            (i = t[u][0]), (o = t[u][1]), (r = t[u][2]);
            for (var a = !0, l = 0; l < i.length; l++)
              (!1 & r || s >= r) &&
              Object.keys(e.O).every(function (t) {
                return e.O[t](i[l]);
              })
                ? i.splice(l--, 1)
                : ((a = !1), r < s && (s = r));
            if (a) {
              t.splice(u--, 1);
              var c = o();
              void 0 !== c && (n = c);
            }
          }
          return n;
        }
        r = r || 0;
        for (var u = t.length; u > 0 && t[u - 1][2] > r; u--) t[u] = t[u - 1];
        t[u] = [i, o, r];
      };
    })(),
    (function () {
      e.n = function (t) {
        var n =
          t && t.__esModule
            ? function () {
                return t["default"];
              }
            : function () {
                return t;
              };
        return e.d(n, { a: n }), n;
      };
    })(),
    (function () {
      e.d = function (t, n) {
        for (var i in n)
          e.o(n, i) &&
            !e.o(t, i) &&
            Object.defineProperty(t, i, { enumerable: !0, get: n[i] });
      };
    })(),
    (function () {
      e.g = (function () {
        if ("object" === typeof globalThis) return globalThis;
        try {
          return this || new Function("return this")();
        } catch (t) {
          if ("object" === typeof window) return window;
        }
      })();
    })(),
    (function () {
      e.o = function (t, n) {
        return Object.prototype.hasOwnProperty.call(t, n);
      };
    })(),
    (function () {
      e.p = "/profile/";
    })(),
    (function () {
      var t = { 143: 0 };
      e.O.j = function (n) {
        return 0 === t[n];
      };
      var n = function (n, i) {
          var o,
            r,
            s = i[0],
            a = i[1],
            l = i[2],
            c = 0;
          if (
            s.some(function (n) {
              return 0 !== t[n];
            })
          ) {
            for (o in a) e.o(a, o) && (e.m[o] = a[o]);
            if (l) var u = l(e);
          }
          for (n && n(i); c < s.length; c++)
            (r = s[c]), e.o(t, r) && t[r] && t[r][0](), (t[r] = 0);
          return e.O(u);
        },
        i = (self["webpackChunkprofilecard"] =
          self["webpackChunkprofilecard"] || []);
      i.forEach(n.bind(null, 0)), (i.push = n.bind(null, i.push.bind(i)));
    })();
  var i = e.O(void 0, [998], function () {
    return e(9518);
  });
  i = e.O(i);
})();
//# sourceMappingURL=app.3bdf6000.js.map
