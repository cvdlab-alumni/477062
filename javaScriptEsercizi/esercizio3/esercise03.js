/*
LEZIONE1: exercise03
write a script that prints in console the 
following multiplication table:
 1,  0,  0,  0,  0,  0,  0,  0,  0,  0
 0,  1,  0,  0,  0,  0,  0,  0,  0,  0
 0,  0,  1,  0,  0,  0,  0,  0,  0,  0
 0,  0,  0,  1,  0,  0,  0,  0,  0,  0
 0,  0,  0,  0,  1,  0,  0,  0,  0,  0
 0,  0,  0,  0,  0,  1,  0,  0,  0,  0
 0,  0,  0,  0,  0,  0,  1,  0,  0,  0
 0,  0,  0,  0,  0,  0,  0,  1,  0,  0
 0,  0,  0,  0,  0,  0,  0,  0,  1,  0
 0,  0,  0,  0,  0,  0,  0,  0,  0,  1
***************************************************************/
var i,j;
var a = "";
var virgola = ",";
var zero;
for(i=1; i<=10; i++) {
	for(j=1; j<=10; j++){
		zero=0;
			if(j==10){
				virgola = "";
			}
			if(i==j){
				zero=1;		
			}
			a = a+(1*zero)+virgola+'\t';
		}
	console.log(a);
	a = "";
	virgola = ",";
}



