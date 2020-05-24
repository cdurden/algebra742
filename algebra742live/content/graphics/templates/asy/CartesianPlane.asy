import geometry;
unitsize(10mm);
draw(({{ min_x }},0)--({{ max_x }},0), arrow=Arrows);
draw((0,{{ min_y }})--(0,{{ max_y }}), arrow=Arrows);
for (int i={{ min_x }}; i<{{ max_x }}; i=i+{{step_x}})
{
  path tick = (0,0.05cm) -- (0cm,-0.05cm);
  pair p = (i,0);
  draw(p+(0, {{ max_y }}) -- p+(0, {{ min_y }}), linetype("0 4"));
  draw(p, tick);
  label(format("$%d$",i), p, S);
}
for (int i={{ min_y }}; i<{{ max_y }}; i=i+{{step_y}})
{
  path tick = (0.05cm,0) -- (-0.05cm,0);
  pair p = (0,i);
  draw(p+({{ max_x }},0) -- p+({{ min_x }},0), linetype("0 4"));
  draw(p, tick);
  label(format("$%d$",i), p, W);
}
