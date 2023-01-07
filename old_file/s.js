var _k = _k || {};
_k.stickyHeaderOptions = {
  type: "autohide",
  containerElement: ".site-header",
  logoElement: ".logo-image",
  triggerOffset: 0,
  offset: ".top-header-bar",
  animationOffset: 10,
  spacer: true,
  animateProgressWithScroll: true,
  animateDuration: null,
  tweenChanges: false,
  classes: {
    name: "site-header",
    prefix: "sticky",
    init: "initialized",
    fixed: "fixed",
    absolute: "absolute",
    spacer: "spacer",
    active: "active",
    fullyActive: "fully-active",
  },
  autohide: {
    animationType: "fade",
    duration: 0.299999999999999988897769753748434595763683319091796875,
    threshold: 100,
  },
  animateScenes: {
    "sticky-logo": {
      name: "sticky-logo",
      selector: "logo",
      props: ["width", "height"],
      css: { width: 38, height: 38 },
      data: {
        type: "alternate-logo",
        alternateLogo: "sticky",
        tags: ["logo-switch"],
      },
      position: 0,
    },
  },
  alternateLogos: {
    sticky: {
      name: "sticky",
      image:
        '<img width="64" height="64" src="https://demo.kaliumtheme.com/photography/wp-content/uploads/2015/11/photography-favicon.png" class="attachment-original size-original" alt="" decoding="async" loading="lazy" srcset="https://demo.kaliumtheme.com/photography/wp-content/uploads/2015/11/photography-favicon.png 64w, https://demo.kaliumtheme.com/photography/wp-content/uploads/2015/11/photography-favicon-30x30.png 30w" sizes="(max-width: 64px) 100vw, 64px" />',
    },
  },
  supportedOn: { desktop: 1, tablet: 1, mobile: 1 },
  other: { menuSkin: null },
  debugMode: false,
};
var _k = _k || {};
_k.logoSwitchOnSections = [];
var _k = _k || {};
_k.enqueueAssets = {
  js: {
    "light-gallery": [
      {
        src: "https://demo.kaliumtheme.com/photography/wp-content/themes/kalium/assets/vendors/light-gallery/lightgallery-all.min.js",
      },
    ],
    videojs: [
      {
        src: "https://demo.kaliumtheme.com/photography/wp-content/themes/kalium/assets/vendors/video-js/video.min.js",
      },
    ],
  },
  css: {
    "light-gallery": [
      {
        src: "https://demo.kaliumtheme.com/photography/wp-content/themes/kalium/assets/vendors/light-gallery/css/lightgallery.min.css",
      },
      {
        src: "https://demo.kaliumtheme.com/photography/wp-content/themes/kalium/assets/vendors/light-gallery/css/lg-transitions.min.css",
      },
    ],
    videojs: [
      {
        src: "https://demo.kaliumtheme.com/photography/wp-content/themes/kalium/assets/vendors/video-js/video-js.min.css",
      },
    ],
  },
};
var _k = _k || {};
_k.require = function (e) {
  var t = e instanceof Array ? e : [e],
    r = function (e) {
      var t, t;
      e.match(/\.js(\?.*)?$/)
        ? ((t = document.createElement("script")).src = e)
        : (((t = document.createElement("link")).rel = "stylesheet"),
          (t.href = e));
      var r = !1,
        a = jQuery("[data-deploader]").each(function (t, a) {
          (e != jQuery(a).attr("src") && e != jQuery(a).attr("href")) ||
            (r = !0);
        }).length;
      r || (t.setAttribute("data-deploader", a), jQuery("head").append(t));
    },
    a;
  return new Promise(function (e, a) {
    var n = 0,
      c = function (t) {
        if (t && t.length) {
          var a = t.shift(),
            n = a.match(/\.js(\?.*)?$/) ? "script" : "text";
          jQuery
            .ajax({ dataType: n, url: a, cache: !0 })
            .success(function () {
              r(a);
            })
            .always(function () {
              a.length && c(t);
            });
        } else e();
      };
    c(t);
  });
};
