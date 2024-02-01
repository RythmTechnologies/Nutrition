const spring = 0.2;
const friction = 0.75;
let pairs = [];

class pathsPair {
  constructor(thePath, thin, fat) {
    this.path = thePath;
    this.thin = thin;
    this.fat = fat;
    this.vals = this.getArgsRy(thin);
    this.target = this.getArgsRy(fat);
    this.vel = this.initRy();
  }
  
  initRy(){
    let Ry = [];
    this.vals.map((t) =>{
      let ry = [];
      t.map(()=>{
        ry.push(0);
      });
      Ry.push(ry)
    });
    return Ry;
  }
  
  getArgsRy(path) {
    let d = path.getAttribute("d").replace(/\r?\n|\r/g, ""); //remove breaklines
    if (d.charAt(0) == "m") {
      d = "M" + d.slice(1);
    }
    let argsRX = /(?=[a-zA-Z])/;
    let args = d.split(argsRX);

    //console.log(args)

    let ArgsRy = [];

    args.map(arg => {
      let argRy = arg
        .slice(1)
        .replace(/\-/g, " -")
        .split(/[ ,]+/);
      argRy.map((p, i) => {
        if (p == "") {
          argRy.splice(i, 1);
        }
      });
      //argRy.map((e) =>{e = parseFloat(e); console.log(e)})
      for(let i = 0; i < argRy.length; i++){
        argRy[i] = parseFloat(argRy[i]);
      }
      
      argRy.unshift(arg[0]);
      ArgsRy.push(argRy);
    });

    return ArgsRy;
  }
  
  morph(){
    let newD = "";
    
    this.vals.map((v,vi) =>{
      
      let newStr = v[0];
      for(let i = 1; i < v.length; i++){
       
        this.updateProp(vi,i);
        
        newStr += v[i].toFixed(3) + " "
      }
      newD += newStr+" ";
    });//
   this.path.setAttributeNS(null,"d", newD);
   //console.log(newD);
  }
  
  updateProp(vi,i) {// reescribir 2 array anidados!!!!!
    let dist  = this.target[vi][i] - this.vals[vi][i];
    let acc = dist * spring;
    this.vel[vi][i] += acc;
    this.vel[vi][i] *= friction;
    this.vals[vi][i] += this.vel[vi][i];
    //this.reStyle();
    } 
   
  goFat(){this.target = this.getArgsRy(this.fat)}
  
  goFit(){this.target = this.getArgsRy(this.thin)}
}

pairs.push(new pathsPair(leg1, leg1_thin,leg1_fat));
pairs.push(new pathsPair(leg2, leg2_thin,leg2_fat));
pairs.push(new pathsPair(shue1, shue1_thin,shue1_fat));
pairs.push(new pathsPair(shue2, shue2_thin,shue2_fat));
pairs.push(new pathsPair(neckline, neckline_thin,neckline_fat));
pairs.push(new pathsPair(hand1, hand1_thin,hand1_fat));
pairs.push(new pathsPair(hand2, hand2_thin,hand2_fat));
pairs.push(new pathsPair(dress, dress_thin,dress_fat));
pairs.push(new pathsPair(wig, wig_thin,wig_fat));
pairs.push(new pathsPair(face, face_thin,face_fat));
pairs.push(new pathsPair(bangs, bangs_thin,bangs_fat));

function Frame() {
rid = window.requestAnimationFrame(Frame);

pairs.map((pair) => pair.morph());
  
  
if(pairs[0].target[7][6] - pairs[0].vals[7][6] == 0){
  window.cancelAnimationFrame(rid); rid = null;
}
}
Frame();


var element = document.getElementById('svg'); // Hover etkileşimini eklemek istediğiniz element

element.addEventListener("mouseover", function() {
  if (rid) {
    window.cancelAnimationFrame(rid);
    rid = null;
  }
  pairs.map((pair) => pair.goFit());
  Frame();
});

element.addEventListener("mouseout", function() {
  if (rid) {
    window.cancelAnimationFrame(rid);
    rid = null;
  }
  pairs.map((pair) => pair.goFat());
  Frame();
});






