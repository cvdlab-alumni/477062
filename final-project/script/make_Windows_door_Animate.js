function make_Windows_door_Animate(){
	//entry door: posperno = 1 perno a destra - posperno = 0 perno a sinistra
  posperno = 1;
  var doorEntry = buildDoor_windows(125,10,276,4,20,20,0x000000,"doorTexture.jpg",posperno);
  hingle = doorEntry.parent;
  hingle.position.set(155,9,276/2+20.01);

  //bathroom door
  posperno = 2;
  var doorBath = buildDoor_windows(127,10,272,4,20,20,0x000000,"bathDoor.jpg",posperno);
  hingle = doorBath.parent;
  hingle.position.set(166,528,276/2+20.01);
  //room door
  posperno = 0;
  var doorRoom = buildDoor_windows(126,10,276,4,20,20,0x000000,"doorTexture.jpg",posperno);
  hingle = doorRoom.parent;
  hingle.position.set(-65,440,276/2+20.01);
  hingle.rotation.z = Math.PI/2;
  //window right-half right side
  posperno = 1;
  var windowRightsideRight = buildDoor_windows(80,10,180,4,20,20,0x000000,"windows.jpg",posperno);
  hingle = windowRightsideRight.parent;
  hingle.position.set(466,9,180/2+130);
  posperno = 2;
  //left side
  var windowRightsideLeft = buildDoor_windows(87.1,10,180,4,20,20,0x000000,"windows.jpg",posperno);
  hingle = windowRightsideLeft.parent;
  hingle.position.set(299,9,180/2+130);
  //window left-half right side
  posperno = 1;
  var windowLeftsideRight = buildDoor_windows(160,10,155,4,20,20,0x000000,"windows.jpg",posperno);
  hingle = windowLeftsideRight.parent;
  hingle.position.set(-319,9,180/2+195);

  //window left-half right side
  posperno = 3;
  var windowBathRoom = buildDoor_windows(75,10,180,4,20,20,0x000000,"windows.jpg",posperno);
  hingle = windowBathRoom.parent;
  windowBathRoom.rotation.z = Math.PI/2;
  hingle.position.set(610,738,155/2+105);

  //out door
  posperno = 1;
  var outDoor = buildDoor_windows(160,10,250,4,20,20,0x000000,"outDoorTexture.jpg",posperno);
  hingle = outDoor.parent;
  hingle.position.set(100,-800,250/2+15.1);

  var objects = [doorEntry, doorBath, doorRoom, windowRightsideRight,windowRightsideLeft,
  windowLeftsideRight,windowBathRoom,outDoor];
  return objects;
}