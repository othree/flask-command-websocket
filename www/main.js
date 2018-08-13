/* */

document.getElementById('run').onclick = function () {
  var output = document.getElementById('output');
  var socket = new WebSocket(`ws://${document.location.host}/job`);
  socket.onmessage = function (event) {
    output.appendChild(document.createTextNode(event.data));
    output.appendChild(document.createTextNode('\n'));
    document.documentElement.scrollTop = document.body.offsetHeight;
  };
  socket.onopen = function (event) {
    socket.send('run');
  };
};

