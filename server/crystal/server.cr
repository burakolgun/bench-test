require "http/server"

PORT = 5000

server = HTTP::Server.new do |context|
  context.response.content_type = "text/html"
  context.response.puts(File.read("./index.html"))
end

address = server.bind_tcp PORT
puts "Listening on http://#{address}"
server.listen