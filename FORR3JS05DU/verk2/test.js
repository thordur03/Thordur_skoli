
let text = [];
for (let count = 0; count < 90; count++) {
	text.push(count);
}
console.log(text);


function makeGrid(screenW,screenH){
	for(let i=0; i < screenW;i+=100) {
	  ctx.beginPath();
	  ctx.moveTo(i,0);
	  ctx.lineTo(i,screenW);
	  ctx.stroke();
	}
	
	for(let i=0; i < screenH;i+=100) {
	  ctx.beginPath();
	  ctx.moveTo(0,i);
	  ctx.lineTo(ScreenH,i);
	  ctx.stroke();
	}
	
	
	ctx.fillStyle = "rgb(200,0,0)";
	ctx.beginPath();
	ctx.arc(screenW/2,ScreenH/2,2,0,Math.PI*2,true);
	ctx.fill();
	
  }