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
