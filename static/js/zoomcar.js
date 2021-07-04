function command(cmd) {
  const message = document.getElementById("message");
  message.innerHTML = "";

  const endpoint = document.getElementById("endpoint").value;
  if (!endpoint) {
    message.innerHTML = "Zoom Car の URL をセットしてください";
    return;
  }
  const XHR = new XMLHttpRequest();
  XHR.addEventListener('load', (event) => {
    console.log(event);
  });

  XHR.addEventListener('error', (event) => {
    message.innerHTML = "有効な Zoom Car の URL をセットしてください";
  });

  XHR.open('POST', `${endpoint}/move/${cmd}`);
  XHR.setRequestHeader('Content-Type', 'application/json');
  XHR.send();
}