/* global _ */

/*
 * Complex scripted dashboard
 * This script generates a dashboard object that Grafana can load. It also takes a number of user
 * supplied URL parameters (in the ARGS variable)
 *
 * Global accessible variables
 * window, document, $, jQuery, ARGS, moment
 *
 * Return a dashboard object, or a function
 *
 * For async scripts, return a function, this function must take a single callback function,
 * call this function with the dashboard object
 */

'use strict';

// accessible variables in this scope
var window, document, ARGS, $, jQuery, moment, kbn;

function make_sync_ajax_req(url, headers={}) {
  var res;

  $.ajax({
    dataType: "json",
    url: url,
    async: false,
    headers: headers,
    success: function(data) {
      res = data;
    }
  }).fail(function(reason) {
    console.info(reason);
  });

  return res;
}

return function(callback) {
  var base_url = window.location.origin;
  var dashboard = make_sync_ajax_req(base_url + "/public/panels/vistual.json");

  $.ajax({
    method: 'GET',
    url: '/'
  }).done(function(result) {

    // when dashboard is composed call the callback
    // function and pass the dashboard
    callback(dashboard);
  });
}
