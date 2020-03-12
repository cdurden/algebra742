struct Shape {
  void draw();
  real area();
}
Shape rectangle(real w, real h) {
  Shape s=new Shape;
  s.draw = new void () {
  draw((0,0)--(w,0)--(w,h)--(0,h)--cycle); };
  s.area = new real () { return w*h; };
  return s;
}
Shape box() {
  Shape s=new Shape;
  s.draw = new void () {
  draw((47,-10)--(53,-10)--(53,-17)--(47,-17)--cycle); };
  s.area = new real () { return 49; };
  return s;
}
rectangle(100,10).draw();
path p=brace((100,-2), (0,-2),5);
draw(p,dashed);
box().draw();
