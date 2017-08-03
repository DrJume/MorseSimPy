// Optional. You will see this name in eg. 'ps' or 'top' command
process.title = 'node-morse-sim-py'

var webSocketsServerPort = 8080

var WebSocketServer = require('websocket').server
var http = require('http')

// list of currently connected clients (users)
var clients = []

var server = http.createServer(function (request, response) {
  // Not important for us. We're writing WebSocket server,
  // not HTTP server
})
server.listen(webSocketsServerPort, function () {
  console.log((new Date()) + ' Server is listening on port ' + webSocketsServerPort)
})

var wsServer = new WebSocketServer({
  httpServer: server
})

wsServer.on('request', function (request) {
  console.log((new Date()) + ' Connection from origin ' + request.origin + '.')

  var connection = request.accept(null, request.origin)

  var index = clients.push(connection) - 1

  console.log((new Date()) + ' ' + connection.remoteAddress + ': Connection accepted.')

  connection.on('message', function (message) {
    if (message.type === 'utf8') {
      console.log(message.utf8Data)
      // broadcast message to all connected clients
      for (var i = 0; i < clients.length; i++) {
        if (i === index) continue
        clients[i].sendUTF(message.utf8Data)
      }
    }
  })
  connection.on('close', function () {
    console.log((new Date()) + ' Peer ' + connection.remoteAddress + ' disconnected.')

    clients.splice(index, 1)
  })
})
