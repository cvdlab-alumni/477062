function buildDoor_windows(xBox,yBox,zBox,rSphere,div1Sphere,div2Sphere,colorSphere,texture,posperno){
      
      var image = THREE.ImageUtils.loadTexture("assets/textures/general/"+texture);
      image.wrapS = image.wrapT = THREE.RepeatWrapping; 
      //image.repeat.set(6,3);
      var boxMaterial = new THREE.MeshBasicMaterial({map:image, side:THREE.DoubleSide});
      var boxGeometry = new THREE.BoxGeometry(xBox,yBox,zBox);
      var box = new THREE.Mesh(boxGeometry, boxMaterial);
      box.castShadow = true;
      if(posperno===1){
        box.interact = function () {
          if(box.parent.rotation.z === 0){
            var translatebox  = new TWEEN.Tween(hinge.rotation)
            .to({x:0, y:0, z: -Math.PI/2},4000)
            .easing(TWEEN.Easing.Bounce.Out)
            .start();
          }
            else{
              var translatebox = new TWEEN.Tween(hinge.rotation)
              .to({x:0, y: 0, z:0},4000)
              .easing(TWEEN.Easing.Bounce.Out)
              .start();   
            }
        }
      var hinge = getSphere(rSphere,div1Sphere,div2Sphere,colorSphere);
      var hingeUp = hinge.clone();
      var hingeDown = hinge.clone();
      hingeUp.position.set(0,0,zBox/3);
      hingeDown.position.set(0,0,-zBox/3);
      box.position.set(-xBox/2,0,0);
      hinge.add(box);
      hinge.add(hingeDown);
      hinge.add(hingeUp);
      }
      else if(posperno===2){
        box.interact = function () {
          if(box.parent.rotation.z === 0){
            var translatebox  = new TWEEN.Tween(hinge.rotation)
            .to({x:0, y:0, z: Math.PI/2},4000)
            .easing(TWEEN.Easing.Bounce.Out)
            .start();
          }
            else{
              var translatebox = new TWEEN.Tween(hinge.rotation)
              .to({x:0, y: 0, z:0},4000)
              .easing(TWEEN.Easing.Bounce.Out)
              .start();   
            }
        }
      var hinge = getSphere(rSphere,div1Sphere,div2Sphere,colorSphere);
      var hingeUp = hinge.clone();
      var hingeDown = hinge.clone();
      hingeUp.position.set(0,0,zBox/3);
      hingeDown.position.set(0,0,-zBox/3);
      box.position.set(xBox/2,0,0);
      hinge.add(box);
      hinge.add(hingeDown);
      hinge.add(hingeUp);
      }
      else if(posperno===0){
         box.interact = function () {
          if(box.parent.rotation.z === 0){
            var translatebox  = new TWEEN.Tween(hinge.rotation)
            .to({x:0, y:0, z: Math.PI/2},4000)
            .easing(TWEEN.Easing.Bounce.Out)
            .start();
          }
            else{
              var translatebox = new TWEEN.Tween(hinge.rotation)
              .to({x:0, y: 0, z:0},4000)
              .easing(TWEEN.Easing.Bounce.Out)
              .start();
            }
      }
      var hinge = getSphere(rSphere,div1Sphere,div2Sphere,colorSphere);
      var hingeUp = hinge.clone();
      var hingeDown = hinge.clone();
      hingeUp.position.set(0,0,zBox/3);
      hingeDown.position.set(0,0,-zBox/3);
      box.position.set(-xBox/2,0,0);
      hinge.add(box);
      hinge.add(hingeDown);
      hinge.add(hingeUp);
      }
      else if(posperno===3){//
         box.interact = function () {
          if(box.parent.rotation.y === 0){
            var translatebox  = new TWEEN.Tween(hinge.rotation)
            .to({x:0, y:-Math.PI/9, z: 0},4000)
            .easing(TWEEN.Easing.Bounce.Out)
            .start();
          }
            else{
              var translatebox = new TWEEN.Tween(hinge.rotation)
              .to({x:0, y: 0, z:0},4000)
              .easing(TWEEN.Easing.Bounce.Out)
              .start();
            }
      }
      var hinge = getSphere(rSphere,div1Sphere,div2Sphere,colorSphere);
      var hingeUp = hinge.clone();
      var hingeDown = hinge.clone();
      hingeUp.position.set(0,xBox/3,0);
      hingeDown.position.set(0,-xBox/3,0);
      box.position.set(0,0,zBox/2);
      hinge.add(box);
      hinge.add(hingeDown);
      hinge.add(hingeUp);
      }
      return box;
}