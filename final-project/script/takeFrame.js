/*make frame in window and door*/
function takeFrame(frame){
	//frame
      //door frame vertical
      var door  = new THREE.Object3D();
      frame.add(door);
      h = 287;
      l = 10;
      s = 20;
      colorBox = 0x81582F;
      var cor1 = getBox(l,s,h,colorBox);
      cor1.position.set(l+15,s/2-.2,h/2+20);
      cor2 = cor1.clone();
      cor2.position.set(l+150,s/2-.2,h/2+20);
      door.add(cor1);
      door.add(cor2);
      //horizontal
      h = 11;
      l = 125;
      s = 20;
      colorBox = 0x81582F;
      cor2 = getBox(l,s,h,colorBox);
      cor2.position.set(l/2+30.1,s/2-.2,h/2+296);
      door.add(cor2);

      //window right frame vertical
      var windowRight  = new THREE.Object3D();
      frame.add(windowRight);
      h = 201;
      l = 10;
      s = 20;
      colorBox = 0x81582F;
      var cor1 = getBox(l,s,h,colorBox);
      cor1.position.set(l/2+290,s/2-.2,h/2+120);
      cor2 = cor1.clone();
      cor2.position.set(l/2+465,s/2-.2,h/2+120);
      windowRight.add(cor1);
      windowRight.add(cor2);
      //horizontal
      h = 10;
      l = 165;
      s = 20;
      colorBox = 0x81582F;
      var cor1 = getBox(l,s,h,colorBox);
      cor1.position.set(l/2+300,s/2-.2,h/2+120);
      cor2 = cor1.clone();
      cor2.position.set(l/2+300,s/2-.2,h/2+311);
      windowRight.add(cor1);
      windowRight.add(cor2);

      //window left frame vertical
      var windowLeft  = new THREE.Object3D();
      frame.add(windowLeft);
      h = 177;
      l = 10;
      s = 20;
      colorBox = 0x81582F;
      var cor1 = getBox(l,s,h,colorBox);
      cor1.position.set(l/2-318,s/2-.2,h/2+198);
      cor2 = cor1.clone();
      cor1.position.set(l/2-488,s/2-.2,h/2+198);
      windowLeft.add(cor1);
      windowLeft.add(cor2);
      //horizontal
      h = 10;
      l = 161.99;
      s = 20;
      colorBox = 0x81582F;
      var cor1 = getBox(l,s,h,colorBox);
      cor1.position.set(l/2-479.99,s/2-.2,h/2+198);
      cor2 = cor1.clone();
      cor2.position.set(l/2-479.99,s/2-.2,h/2+365);
      windowLeft.add(cor1);
      windowLeft.add(cor2);

      //window bathroom frame vertical
      var windowbathroom  = new THREE.Object3D();
      frame.add(windowbathroom);
      h = 201;
      l = 20;
      s = 10;
      colorBox = 0x81582F;
      var cor1 = getBox(l,s,h,colorBox);
      cor1.position.set(l/2+600,695,h/2+169.5);
      cor2 = cor1.clone();
      cor2.position.set(l/2+600,780,h/2+169.5);
      windowbathroom.add(cor1);
      windowbathroom.add(cor2);
      //horizontal
      h = 10;
      l = 20;
      s = 75.5;
      colorBox = 0x81582F;
      var cor1 = getBox(l,s,h,colorBox);
      cor1.position.set(l/2+600,737,h/2+169.5);
      cor2 = cor1.clone();
      cor2.position.set(l/2+600,737,h/2+360);
      windowbathroom.add(cor1);
      windowbathroom.add(cor2);

      //bathroom door frame vertical
      var door  = new THREE.Object3D();
      frame.add(door);
      h = 285.5;
      l = 10;
      s = 20;
      colorBox = 0x81582F;
      var cor1 = getBox(l,s,h,colorBox);
      cor1.position.set(l+151,s/2+518,h/2+20);
      cor2 = cor1.clone();
      cor2.position.set(l+288.5,s/2+518,h/2+20);
      door.add(cor1);
      door.add(cor2);
      //horizontal
      h = 11;
      l = 128;
      s = 20;
      colorBox = 0x81582F;
      cor2 = getBox(l,s,h,colorBox);
      cor2.position.set(l/2+166,s/2+518,h/2+294);
      door.add(cor2);

      //room door frame vertical
      var door  = new THREE.Object3D();
      frame.add(door);
      h = 285.5;
      l = 25;
      s = 10;
      colorBox = 0x81582F;
      var cor1 = getBox(l,s,h,colorBox);
      cor1.position.set(l-90,s/2+439,h/2+20);
      cor2 = cor1.clone();
      cor2.position.set(l-90,s/2+305,h/2+20);
      door.add(cor1);
      door.add(cor2);
      //horizontal
      h = 10;
      l = 25;
      s = 125;
      colorBox = 0x81582F;
      cor2 = getBox(l,s,h,colorBox);
      cor2.position.set(l-90,s/2+315,h/2+295);
      door.add(cor2);
}


function takeRoof(lung,larg,spessore,colorBox,model){
      roof = getRoofBox(lung,larg,spessore,colorBox);
      roof.position.set(0,lung/2-300,420+5);
      model.add(roof);
}


function makeOutPlane(model,textureOutPlane,x,y,h){
      var image = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureOutPlane);
      image.wrapS = image.wrapT = THREE.RepeatWrapping; 
      image.repeat.set(5,5);
      var grassMaterial = new THREE.MeshPhongMaterial( { map: image, side: THREE.DoubleSide});
      var grassGeometry = new THREE.BoxGeometry(x, y, h);
      var grassPlane = new THREE.Mesh(grassGeometry, grassMaterial);
      grassPlane.position.set(0,0,-h/2+15);
      grassPlane.receiveShadow = true;
      model.add(grassPlane);
}

function getCarpet(x,y,textureCarpet){
      var image = new THREE.ImageUtils.loadTexture( "assets/textures/general/"+textureCarpet);
      image.wrapS = image.wrapT = THREE.RepeatWrapping; 
      //image.repeat.set(10,10);
      var carpetMaterial = new THREE.MeshLambertMaterial( { map: image, side: THREE.DoubleSide});
      var carpetGeometry = new THREE.PlaneGeometry(x, y);
      var carpet = new THREE.Mesh(carpetGeometry, carpetMaterial);
      //carpet.position.set(100,-120,0);
      return carpet;
}