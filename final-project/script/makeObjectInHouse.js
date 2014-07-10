
//take bathroom object
function makeObjectInBathRoom(otherObjObject){
	//import washbowl(lavandino) in bathroom
	var washbowl = importOtherObjectModel("bathroom1.obj","bathroom1.mtl");
	washbowl.scale.set(1.5, 1, 1);
	washbowl.position.set(180, 840, 25);
	washbowl.rotation.x = Math.PI/2;
	otherObjObject.add(washbowl);
	//import doccia in bathroom
	var doccia = importOtherObjectModel("doccia.obj","doccia.mtl");
	doccia.scale.set(1.5, 1.5, 1.5);
	doccia.position.set(-1, 540, 20.01);
	doccia.rotation.x = Math.PI/2;
	otherObjObject.add(doccia);
	//import bidet in bathroom
	var bidet = importOtherObjectModel("bidet.obj","bidet.mtl");
	bidet.scale.set(2, 2, 2);
	bidet.position.set(550, 780, 20.01);
	bidet.rotation.x = Math.PI/2;
	otherObjObject.add(bidet);
	//import washingMachine in bathroom
	var washingMachine = importOtherObjectModel("washingMachine.obj","washingMachine.mtl");
	washingMachine.scale.set(1.5, 1.5, 1.5);
	washingMachine.position.set(360, 800, 84);
	washingMachine.rotation.x = Math.PI/2;
	otherObjObject.add(washingMachine);
	//import shower of doccia in bathroom
	var shower = importOtherObjectModel("shower.obj","shower.mtl");
	shower.scale.set(1.5, 1.5, 1.5);
	shower.position.set(550, 540, 20.01);
	shower.rotation.x = Math.PI/2;
	shower.rotation.y = Math.PI;
	otherObjObject.add(shower);
	//import toilet in bathroom
	var toilet = importOtherObjectModel("toilet.obj","toilet.mtl");
	toilet.scale.set(2, 2, 2);
	toilet.position.set(550, 850, 20.01);
	toilet.rotation.x = Math.PI/2;
	otherObjObject.add(toilet);
}
/*-----------------------------------------------*/
function makeObjectInLivingRoom(otherObjObject){
//take a sofa in living room
  var sofa = importOtherObjectModel("sofa.obj","sofa.mtl");
  sofa.scale.set(1, 1, 1);
  sofa.position.set(590, 350, 20.01);
  sofa.rotation.x = Math.PI/2;
  sofa.rotation.y = -Math.PI/2;
  otherObjObject.add(sofa);
  //take a bed in living room
  var bedLivingRoom = importOtherObjectModel("livingRoomBed.obj","livingRoomBed.mtl");
  bedLivingRoom.scale.set(1, 1, 1);
  bedLivingRoom.position.set(500, 480, 20.01);
  bedLivingRoom.rotation.x = Math.PI/2;
  bedLivingRoom.rotation.y = -Math.PI/2;
  otherObjObject.add(bedLivingRoom);
  //take a radiator in living room
  var radiator = importOtherObjectModel("radiator.obj","radiator.mtl");
  radiator.scale.set(1, 1, 1);
  radiator.position.set(400, 35, 20);
  radiator.rotation.x = Math.PI/2;
  otherObjObject.add(radiator);
	//take a orient carpet in living room
  var carpetLivingRoom = importOtherObjectModel("carpetOrientLivingRoom.obj","carpetOrientLivingRoom.mtl");
  carpetLivingRoom.scale.set(.6, .6, .6);
  carpetLivingRoom.position.set(300,265,21);
  carpetLivingRoom.rotation.x = Math.PI/2;
  otherObjObject.add(carpetLivingRoom);
  //take a bed blu in living room
  var bedBlueLivingRoom = importOtherObjectModel("bedBlue.obj","bedBlue.mtl");
  bedBlueLivingRoom.scale.set(1, 1, 1);
  bedBlueLivingRoom.position.set(970, 340, 20.01);
  bedBlueLivingRoom.rotation.x = Math.PI/2;
  bedBlueLivingRoom.rotation.y = -Math.PI/2;
  otherObjObject.add(bedBlueLivingRoom);
  //take a table in living room
  var tableLivinigRoom = importOtherObjectModel("table.obj","table.mtl");
  tableLivinigRoom.scale.set(1, 1, 1);
  tableLivinigRoom.position.set(300,265,20.01);
  tableLivinigRoom.rotation.x = Math.PI/2;
  tableLivinigRoom.rotation.y = -Math.PI/2;
  otherObjObject.add(tableLivinigRoom);
  //take a chair in living room up
  var chairLivinigRoom = importOtherObjectModel("chair.obj","chair.mtl");
  chairLivinigRoom.scale.set(1, 1, 1);
  chairLivinigRoom.position.set(300,370,20.01);
  chairLivinigRoom.rotation.x = Math.PI/2;
  otherObjObject.add(chairLivinigRoom);
  //take a chair in living room right
  var chairLivinigRoom = importOtherObjectModel("chair.obj","chair.mtl");
  chairLivinigRoom.scale.set(1, 1, 1);
  chairLivinigRoom.position.set(370,260,20.01);
  chairLivinigRoom.rotation.x = Math.PI/2;
  chairLivinigRoom.rotation.y = -Math.PI/2;
  otherObjObject.add(chairLivinigRoom);
  //take a chair in living room left
  var chairLivinigRoom = importOtherObjectModel("chair.obj","chair.mtl");
  chairLivinigRoom.scale.set(1, 1, 1);
  chairLivinigRoom.position.set(200,260,20.01);
  chairLivinigRoom.rotation.x = Math.PI/2;
  chairLivinigRoom.rotation.y = Math.PI/2;
  otherObjObject.add(chairLivinigRoom);
  //take a chair in living room down
  var chairLivinigRoom = importOtherObjectModel("chair.obj","chair.mtl");
  chairLivinigRoom.scale.set(1, 1, 1);
  chairLivinigRoom.position.set(300,170,20.01);
  chairLivinigRoom.rotation.x = Math.PI/2;
  chairLivinigRoom.rotation.y = Math.PI;
  otherObjObject.add(chairLivinigRoom);
  //female sit on chair
  var femaleSitOnChair = importOtherObjectModel("FemaleSitLivingRoom.obj","FemaleSitLivingRoom.mtl");
  femaleSitOnChair.scale.set(1, 1, 1);
  femaleSitOnChair.position.set(300,174,23);
  femaleSitOnChair.rotation.x = Math.PI/2;
  femaleSitOnChair.rotation.y = Math.PI/2;
	otherObjObject.add(femaleSitOnChair);
  //male sit on chair
  var maleSitOnChair = importOtherObjectModel("sitMaleLivingRoom.obj","sitMaleLivingRoom.mtl");
  maleSitOnChair.scale.set(1, 1, 1);
  maleSitOnChair.position.set(200,260,20.01);
  maleSitOnChair.rotation.x = Math.PI/2;
  maleSitOnChair.rotation.y = Math.PI/2;
  otherObjObject.add(maleSitOnChair);
  //male sit on land
  var maleSitOnLand = importOtherObjectModel("sitMaleOnLand.obj","sitMaleOnLand.mtl");
  maleSitOnLand.scale.set(1, 1, 1);
  maleSitOnLand.position.set(380,200,25);
  maleSitOnLand.rotation.x = Math.PI/2;
  maleSitOnLand.rotation.y = Math.PI/2;
  otherObjObject.add(maleSitOnLand);
	//female sit on land
  var femaleSitOnLand = importOtherObjectModel("femaleSitOnLand.obj","femaleSitOnLand.mtl");
  femaleSitOnLand.scale.set(1, 1, 1);
  femaleSitOnLand.position.set(380,350,23);
  femaleSitOnLand.rotation.x = Math.PI/2;
 	femaleSitOnLand.rotation.y = Math.PI/2;
  otherObjObject.add(femaleSitOnLand);
}

/*-----------------------------------------------*/
//take room object
function makeObjectInRoom(otherObjObject){
	//take sofa in room
	var bedRoom = importOtherObjectModel("sofaRoom.obj","sofaRoom.mtl");
	bedRoom.scale.set(80, 80, 80);
	bedRoom.position.set(-145, 180, 20.01);
	bedRoom.rotation.x = Math.PI/2;
	bedRoom.rotation.y = -Math.PI/2;
	otherObjObject.add(bedRoom);
	//take desk in room
	var deskRoom = importOtherObjectModel("deskRoom.obj","deskRoom.mtl");
	deskRoom.scale.set(1, 1, 1);
	deskRoom.position.set(-560, 200, 20.01);
	deskRoom.rotation.x = Math.PI/2;
	deskRoom.rotation.y = Math.PI/2;
	otherObjObject.add(deskRoom);
	//take wardrobe in room
	var wardrobeRoom = importOtherObjectModel("wardrobe.obj","wardrobe.mtl");
	wardrobeRoom.scale.set(1.5, 1, 1.5);
	wardrobeRoom.position.set(-400, 470, 251);
	wardrobeRoom.rotation.x = -Math.PI/2;
	wardrobeRoom.rotation.y = Math.PI;
	otherObjObject.add(wardrobeRoom);
	//take closet in room between window
	var closetRoom = importOtherObjectModel("closet.obj","closet.mtl");
	closetRoom.scale.set(1, 1, 1);
	closetRoom.position.set(-530, 60, 20.01);
	closetRoom.rotation.x = Math.PI/2;
	closetRoom.rotation.y = Math.PI/2;
	otherObjObject.add(closetRoom);
	//take closet1 in room
	var closet1Room = importOtherObjectModel("closetRoom1.obj","closetRoom1.mtl");
	closet1Room.scale.set(1, 1, 1);
	closet1Room.position.set(-110, 455, 20.01);
	closet1Room.rotation.x = Math.PI/2;
	otherObjObject.add(closet1Room);
	//take carpet in room 
	var carpetRoom = importOtherObjectModel("carpetRoom.obj","carpetRoom.mtl");
	carpetRoom.scale.set(1, 1, 1);
	carpetRoom.position.set(-300, 200, 20.01);
	carpetRoom.rotation.x = Math.PI/2;
	otherObjObject.add(carpetRoom);
	//take a table in room 
	var tableRoom = importOtherObjectModel("tableRoom.obj","tableRoom.mtl");
	tableRoom.scale.set(1, 1, 1);
	tableRoom.position.set(-350, 250, 20.01);
	tableRoom.rotation.x = Math.PI/2;
	otherObjObject.add(tableRoom);
	//take a chair in room 
	var chairRoom = importOtherObjectModel("chairRoom.obj","chairRoom.mtl");
	chairRoom.scale.set(1, 1, 1);
	chairRoom.position.set(-300, 560, 145);
	chairRoom.rotation.x = Math.PI/2;
	chairRoom.rotation.y = -Math.PI/2;
	otherObjObject.add(chairRoom);
	//take a frame in room 
	var tigerFrameRoom = importOtherObjectModel("TigerFrame.obj","TigerFrame.mtl");
	tigerFrameRoom.scale.set(4, 3, 3);
	tigerFrameRoom.position.set(-599.9, 300, 170);
	tigerFrameRoom.rotation.x = Math.PI/2;
	tigerFrameRoom.rotation.y = Math.PI/2;
	otherObjObject.add(tigerFrameRoom);
}

/*-----------------------------------------------*/
//take out house object
function makeObjectOutHouse(otherObjObject){
	var geezer = importOtherObjectModel("geezer.obj","geezer.mtl");
	geezer.scale.set(2, 2.5, 2);
	geezer.position.set(550, -30.1, 250);
	geezer.rotation.x = Math.PI/2;
	otherObjObject.add(geezer);

	wallOut = "wall1.jpg";
	var image = THREE.ImageUtils.loadTexture("assets/textures/general/"+wallOut);
    image.wrapS = image.wrapT = THREE.RepeatWrapping; 
    image.repeat.set(10,4);

    var wallOutMaterial = new THREE.MeshBasicMaterial({map:image, side:THREE.DoubleSide});
    var wallOutGeometry = new THREE.BoxGeometry(940,250,50);
    var wallOutFront = new THREE.Mesh(wallOutGeometry, wallOutMaterial);
   	wallOutFront.position.set(-530,-800,250/2+15.1);
   	wallOutFront.rotation.x = Math.PI/2;
   	otherObjObject.add(wallOutFront);

   	var wallOutGeometry = new THREE.BoxGeometry(900,250,50);
    var wallOutFront = new THREE.Mesh(wallOutGeometry, wallOutMaterial);
   	wallOutFront.position.set(550,-800,250/2+15.1);
   	wallOutFront.rotation.x = Math.PI/2;
   	otherObjObject.add(wallOutFront);
	//lateral
	var image = THREE.ImageUtils.loadTexture("assets/textures/general/"+wallOut);
    image.wrapS = image.wrapT = THREE.RepeatWrapping; 
    image.repeat.set(4,20);
    var wallOutMaterial = new THREE.MeshBasicMaterial({map:image, side:THREE.DoubleSide});
   	var wallOutGeometry = new THREE.BoxGeometry(30,1800,250);
    var wallOutFront = new THREE.Mesh(wallOutGeometry, wallOutMaterial);
   	wallOutFront.position.set(985.01,75.01,250/2+15.1);
   	otherObjObject.add(wallOutFront);

   	var image = THREE.ImageUtils.loadTexture("assets/textures/general/"+wallOut);
    image.wrapS = image.wrapT = THREE.RepeatWrapping; 
    image.repeat.set(4,20);
    var wallOutMaterial = new THREE.MeshBasicMaterial({map:image, side:THREE.DoubleSide});
   	var wallOutGeometry = new THREE.BoxGeometry(30,1800,250);
    var wallOutFront = new THREE.Mesh(wallOutGeometry, wallOutMaterial);
   	wallOutFront.position.set(-985.01,75.01,250/2+15.1);
   	otherObjObject.add(wallOutFront);


	var image = THREE.ImageUtils.loadTexture("assets/textures/general/"+wallOut);
    image.wrapS = image.wrapT = THREE.RepeatWrapping; 
    image.repeat.set(20,4);
   	var wallOutMaterial = new THREE.MeshBasicMaterial({map:image, side:THREE.DoubleSide});
    var wallOutGeometry = new THREE.BoxGeometry(2000,250,50);
    var wallOutFront = new THREE.Mesh(wallOutGeometry, wallOutMaterial);
   	wallOutFront.position.set(0,951,250/2+15.1);
   	wallOutFront.rotation.x = Math.PI/2;
   	otherObjObject.add(wallOutFront);

	//female sit out
	var sitFemale02 = importOtherObjectModel("sitFemale02.obj","sitFemale02.mtl");
	sitFemale02.scale.set(1, 1, 1);
	sitFemale02.position.set(100,-400,30);
	sitFemale02.rotation.x = Math.PI/2;
	sitFemale02.rotation.y = Math.PI/2;
	otherObjObject.add(sitFemale02);

	//three out left
	var weepingWillow = importOtherObjectModel("weepingWillow.obj","weepingWillow.mtl");
	weepingWillow.scale.set(50, 50, 50);
	weepingWillow.position.set(-500,-500,30);
	weepingWillow.rotation.x = Math.PI/2;
	weepingWillow.rotation.y = Math.PI/2;
	otherObjObject.add(weepingWillow);

	//three out right
	var blackTupelo = importOtherObjectModel("blackTupelo.obj","blackTupelo.mtl");
	blackTupelo.scale.set(50, 50, 50);
	blackTupelo.position.set(500,-500,30);
	blackTupelo.rotation.x = Math.PI/2;
	blackTupelo.rotation.y = Math.PI/2;
	otherObjObject.add(blackTupelo);

	//car out 
	var car = importOtherObjectModel("car.obj","car.mtl");
	car.scale.set(10, 10, 10);
	//car.position.set(500,-1000,30);
	car.rotation.x = Math.PI/2;
	car.rotation.y = Math.PI/2;
	var cube = getBoxFrameObject(300,100,150,0xFF0000);
	cube.position.set(500,-1000,20);
	cube.add(car);
	cube.interact = function (){
   		initAnimator();
	    animator.start();
	}
	//animation
    var animator = null;
    var duration = 5;
    var loopAnimation = false;
   	function initAnimator() {
        animator = new KF.KeyFrameAnimator;
        animator.init({ 
        interps:
        [
            { 
            keys:[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,.1], 
            values:[
                {x : 750 },
                {x : 800 },
                {x : 850 },
                {x : 900  },
                {x : 1000 },
                {x : 900 },
                {x : 850 },
                {x : 800 },
                {x : 750 },
                {x : 500 },
                ],
                target:cube.position
                },
            ],
        loop: loopAnimation,
        duration: duration * 1000
        });
        }

	otherObjObject.add(cube);

	//car1 out 
	var car1 = importOtherObjectModel("car1.obj","car1.mtl");
	car1.scale.set(10, 10, 10);
	car1.position.set(-500,-1000,28);
	car1.rotation.x = Math.PI/2;
	car1.rotation.y = Math.PI/2;
	otherObjObject.add(car1);

	function getBoxFrameObject(lung,larg,spessore,colorBox){
    var GeometriaPiano = new THREE.BoxGeometry(lung,larg,spessore);
    var MaterialePiano = new THREE.MeshPhongMaterial({color: colorBox,
        side: THREE.DoubleSide,transparent: true, opacity: .0});
    var box = new THREE.Mesh(GeometriaPiano,MaterialePiano);
    return box;
}
return cube;

}

/*-----------------------------------------------*/
//take kitchen object
function makeObjectInKitchen(otherObjObject){
	//take kitchenIslandDown in kitchen right
	var kitchenIslandDown = importOtherObjectModel("kitchenIslandDown.obj","kitchenIslandDown.mtl");
	kitchenIslandDown.scale.set(2, 1.5, 1);
	kitchenIslandDown.position.set(170, 900, 30);
	kitchenIslandDown.rotation.x = Math.PI/2;
	kitchenIslandDown.rotation.y = -Math.PI/2;
	otherObjObject.add(kitchenIslandDown);
	//take kitchenIslandDown in kitchen left
	var kitchenIslandDown = importOtherObjectModel("kitchenIslandDown.obj","kitchenIslandDown.mtl");
	kitchenIslandDown.scale.set(2, 1.5, 1);
	kitchenIslandDown.position.set(-650, 930, 30);
	kitchenIslandDown.rotation.x = Math.PI/2;
	otherObjObject.add(kitchenIslandDown);
	//take gas in kitchen
	var kitchenIslandDown = importOtherObjectModel("stove.obj","stove.mtl");
	kitchenIslandDown.scale.set(20, 20, 10);
	kitchenIslandDown.position.set(-300, 805, 146);
	kitchenIslandDown.rotation.x = Math.PI/2;
	otherObjObject.add(kitchenIslandDown);
	//take Washbowl(lavandino) in kitchen
	var kitchenWashbowl = importOtherObjectModel("kitchenWashbowl.obj","kitchenWashbowl.mtl");
	kitchenWashbowl.scale.set(1, 1.5, 1);
	kitchenWashbowl.position.set(-215, 790, 14);
	kitchenWashbowl.rotation.x = Math.PI/2;
	otherObjObject.add(kitchenWashbowl);
	//take kitchenIsland(sX lavandino) in kitchen
	var kitchenSxWashbowl = importOtherObjectModel("kitchenSingleCabinet.obj","kitchenSingleCabinet.mtl");
	kitchenSxWashbowl.scale.set(2, 1.5, 1);
	kitchenSxWashbowl.position.set(165, 600, 14);
	kitchenSxWashbowl.rotation.x = Math.PI/2;
	otherObjObject.add(kitchenSxWashbowl);
}