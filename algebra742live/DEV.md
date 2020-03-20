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
