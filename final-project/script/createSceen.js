function createSceen (geom,texture) {
    var materialArray = [];
    materialArray.push(new THREE.MeshBasicMaterial({ color: 0x555555  }));
    materialArray.push(new THREE.MeshBasicMaterial({ color: 0x555555  }));
    materialArray.push(new THREE.MeshBasicMaterial({ color: 0x555555  }));
    materialArray.push(new THREE.MeshBasicMaterial({ color: 0x555555   }));
    materialArray.push(new THREE.MeshBasicMaterial({ map: texture }));
    materialArray.push(new THREE.MeshBasicMaterial({ color: 0xeeee33  }));
    var faceMaterial = new THREE.MeshFaceMaterial(materialArray);
    // create a multimaterial
    var mesh = new THREE.Mesh(geom, faceMaterial);
    return mesh;
}
function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    render.setSize( window.innerWidth, window.innerHeight );
}