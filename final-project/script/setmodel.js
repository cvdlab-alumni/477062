function setmodel(model){
	var GeometriaPiano = new THREE.BoxGeometry(555,1,420);
    var MaterialePiano = new THREE.MeshLambertMaterial({side: THREE.DoubleSide});
    var box = new THREE.Mesh(GeometriaPiano,MaterialePiano);
    box.position.set(-330,540,420/2);
    model.add(box);
}