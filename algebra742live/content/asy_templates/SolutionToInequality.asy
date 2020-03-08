import geometry;
unitsize(10mm);
draw((-3,0)--(10,0), arrow=Arrows);
draw((-3,0)--(5,0), arrow=None, p=gray(0)+1);
draw((5,0), marker=MarkFill[0], p=gray(0)+1);
for (int i=-3; i<10; ++i)
{
  path tick = (0,0) -- (0,-0.15cm);
  pair p = (i,0);
  draw(p, tick);
  label(format("$%d$",i), p, S);
}
