function importLarModel(model,objfile){
	 var mesh;
      var loader = new THREE.OBJLoader();
      loader.load("assets/objModelLar/"+objfile, function (obj) {
        var material = new THREE.MeshLambertMaterial({shading: THREE.FlatShading,
        side: THREE.DoubleSide});
        obj.traverse(function (child) {
          if (child instanceof THREE.Mesh) {
            child.material = material;
          }
        });
        obj.scale.set(100, 100, 100);
        obj.position.set(-1240/2, 0, 0);
        mesh = obj;
        model.add(obj);
      });
}

function importOtherObjectModel(fileobj,filemtl){
  var loader = new THREE.OBJMTLLoader();
  var object3D  = new THREE.Object3D();
  loader.addEventListener('load', function (event) {
    var object = event.content;
    object3D.add(object);
    });
      loader.load(
        'assets/objOtherFile/'+fileobj, 
        'assets/objOtherFile/'+filemtl, 
        {side: THREE.DoubleSide}
      );
      return object3D;
}