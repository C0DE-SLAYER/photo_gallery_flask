/*!
 * jQuery throttle / debounce - v1.1 - 3/7/2010
 * http://benalman.com/projects/jquery-throttle-debounce-plugin/
 * 
 * Copyright (c) 2010 "Cowboy" Ben Alman
 * Dual licensed under the MIT and GPL licenses.
 * http://benalman.com/about/license/
 */
!function(t,n){var $=t.jQuery||t.Cowboy||(t.Cowboy={}),o;$.throttle=o=function(t,o,u,e){function i(){function i(){a=+new Date,u.apply(f,g)}function c(){r=n}var f=this,d=+new Date-a,g=arguments;e&&!r&&i(),r&&clearTimeout(r),e===n&&d>t?i():!0!==o&&(r=setTimeout(e?c:i,e===n?t-d:t))}var r,a=0;return"boolean"!=typeof o&&(e=u,u=o,o=n),$.guid&&(i.guid=u.guid=u.guid||$.guid++),i},$.debounce=function(t,u,e){return e===n?o(t,u,!1):o(t,e,!1!==u)}}(this);