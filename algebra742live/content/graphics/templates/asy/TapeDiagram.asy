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
rectangle(100,10).draw();
