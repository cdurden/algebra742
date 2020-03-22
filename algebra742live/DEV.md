# Collaborative Whiteboard
0. The routing system either generates a random id or looks up a room id given as part of the url. It emits a socket.io call to 'roomId'. When the server receives this call (in server/sockets.js), it adds that member to the room. The addMember method (in server/rooms.js) emits a showExisting call with payload rooms[roomId]. When the client receives this call (in client/services/receive.js), it uses the EventHandler to draw the data onto the board, by calling methods in the ShapeBuilder factory (drawing is done by calling methods on the board object in BoardData). The input handler calls methods from the Broadcast factory which emit socket.io messages to the server (received in server/sockets.js, and stored in redis via server/rooms.js which uses the redis client in server/db/config.js)
1. Fix the UI issues
2. Data for a single whiteboard is stored in a redis string associated with a room id. The string is a JSON encoded representation of the whiteboard data. This string could be saved to a database and reloaded later.
  a0. How to serve the albus whiteboard client through algebra742/Flask and route socket.io data to the node server
  a1. How to set up two separater sockets, one to handle whiteboard actions, and another to handle interaction with algebra742live
  a2. How to process submissions to facilitate feedback. How to integrate Albus with the admin dashboard.
  a. How to associate drawing data with algebra742live users.
    i. send socketId from albus to algebra742live and set up a redis hash mapping socketId to user data. Deal with ensuring that the socketId is mapped before allowing user interaction. When data is swapped between the database and redis, swap the socketId and the user id.
    ii. Have algebra742live act as a proxy to albus server. Set session cookie in request. When user sends data to albus, send the session id, ... 
  b. How to associate drawing data with a DrawingQuestion. Use a room id to associate a DrawingForm with a whiteboard room. Multiple students can be assigned the same room id. When they submit their form, the room id can be submitted and a save operation can transfer the whiteboard into the database and the id field of this tuple can be recorded as part of their answer.
     i. How is collaborative work submitted? Do all students have to agree to submit the work? How can a student save work if a partner does not do anything?
  c. How to add a background image to a drawing? Use the Raphael image method: board.image(src, x, y, width, height)
  d. Is there a way to use mathjax to process tex input and render it using Raphael?
3. 
EdPuzzle
Woot math
Quizizz
https://blog.quizizz.com/our-guide-to-remote-learning-dc6a922c5279
# March 18, 2020 desired features
1. Collaborative whiteboard
see https://github.com/socketio/socket.io/blob/master/examples/whiteboard/public/main.js
Idea: Allow admin to control which users are allowed to modify a particular canvas.
Details:
  a. Create a table of canvases. attributes: id, height, width, data
  b. Set permissions via a many-to-many mapping between canvases and users. canvas_id, user_id, region, permission
  c. Add canvases to the database on question submission. include canvas_id in answer field of question_response
  d. Use socket.io to allow concurrent drawing to canvases.

2. Ability to create a queue of student responses that require manual grading and/or feedback, to notify the teacher of these, and to enable an efficient method for providing feedback, and to notify the student when the feedback is ready to view, and enable the student to view it.
3. Whiteboard zoom
4. Streaming
Overview of the networking issues involved with video conferencing:
https://bloggeek.me/how-many-users-webrtc-call/
Why a media server is necessary:
https://bloggeek.me/media-server-for-webrtc-broadcast/

https://jitsi.org/news/open-source-sfus/

# Developing a live application
Features
1. Interface for an administrator to control the state of the game/session
  a. Set tasks and timers, when the state will change to the next task. Send events to the clients which will trigger a change on their screen (rendering the view of the new task).
  b. Allow depth-of-exploration differentiation. Students can progress through the stages of a multi-part task at their own pace. This would provide students who demonstrate understanding of the basics with an opportunity to dig deeper into a subject. While those students are digging deeper, I can help students develop the basic skills. Once everyone has had time to explore the ideas productively, we can move on to the next subject together.
  c. Allow individualization of tasks. The flow of tasks can be controlled by condition-dependent control structures so that students can do different tasks in parallel. This could be implemented by applying boolean functions to database query results, and associating those functions with bifurcating nodes in a directed graph.
  d. Be able to set an alert so that I know when a certain percentage of students have crossed a threshold.
  e. Allow asymptote figures to be embedded in problems. Implementation suggestions:
    i. add an attribute to each node which associates asymptote templates. Do preprocessing (add a separate script which reads a set of dot files to generate the graphics for them) to generate graphics using the templates and the parameters of the node. The view will then use a consistent pattern to find the generated graphics files.
  f. How can I integrate reveal.js? 
    i. Create a RevealJSMultiPartTask question type which would have a presentation associated with it containing placeholders for question parts.
    ii. Create a RevealJSPresentationGame
  g. Add questions to RevealJSPresentationGame. Insert question markup into 
  h. jquery-mobile only allows one page to be displayed at a time. this prevents me from being able to add jquery-mobile pages to reveal.js slides, and simply transitioning between slides to display the different questions. An alternative solution would be to have one page, and to have a slidechange event detect whether a page contains a question. If so it would move the single jquery-mobile page to the active slide and trigger a question update on that page.
