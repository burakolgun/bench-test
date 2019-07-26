const http = require('http')
const port = 4000
const fs = require('fs');
const requestHandler = (request, response) => {
  fs.readFile('index.html', function(err, data) {
    response.write(data);
    response.end();
})}
const server = http.createServer(requestHandler)
server.listen(port, (err) => {
  if (err) {
    return console.log('something bad happened', err)
  }
  console.log(`server is listening on ${port}`)
})