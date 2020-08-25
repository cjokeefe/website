let button;

function setup() {
  createCanvas(windowWidth, windowHeight);
  //translate(width/2, height/2);
  
  button = createButton('Generate');
  buttonWidth = (button.size().width);
  button.position(width*0.5-(buttonWidth*0.5), height*0.6);
  button.mousePressed(generate);
  
  r1 = round(random(256));
  r2 = round(random(256));
  g1 = round(random(256));
  g2 = round(random(256));
  b1 = round(random(256));
  b2 = round(random(256));
  
  rdif = r2-r1;
  gdif = g2-g1;
  bdif = b2-b1;
  
  rrate=width/rdif;
  grate=width/gdif;
  brate=width/bdif;
}


function generate() {
  clear();
  r1 = round(random(256));
  r2 = round(random(256));
  g1 = round(random(256));
  g2 = round(random(256));
  b1 = round(random(256));
  b2 = round(random(256));
  
  rdif = r2-r1;
  gdif = g2-g1;
  bdif = b2-b1;
  
  rrate=width/rdif;
  grate=width/gdif;
  brate=width/bdif;
}


function draw() {
  for(let i=0; i<width; i++) {
    r = r1 + i/rrate;
    g = g1 + i/grate;
    b = b1 + i/brate;
    stroke(r,g,b);
    line(i,0,i,height/5);
  }
  /**
  let start = '(' + r1.toFixed() + ', ' + g1.toFixed() + ', ' + b1.toFixed() +')';
  let end = '(' + r2.toFixed() + ', ' + g2.toFixed() + ', ' + b2.toFixed() +')';
  **/
  
  let start = rgbToHex(r1, g1, b1);
  let end = rgbToHex(r2, g2, b2);
  
  noStroke();
  textSize(12);
  textAlign(LEFT);
  text(start, 0, height/5 + 12);
  textAlign(RIGHT);
  text(end, width, height/5 + 12);
  
}

function componentToHex(c) {
  var hex = c.toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
  return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}